# -*- coding: utf-8 -*-
import ee
import geemap
import datetime

# Initialize Earth Engine
ee.Initialize()

# Load Himachal boundary (upload your geojson to assets or load locally)
himachal = geemap.shp_to_ee("Himachal_GEOJSON.geojson")

# Define parameters
bands = ['B2', 'B3', 'B4', 'B8', 'B11']  # Blue, Green, Red, NIR, SWIR
start_date = datetime.date(2016, 6, 1)
num_weeks = 14

# Cloud mask function
def maskS2clouds(image):
    qa = image.select('QA60')
    cloudBitMask = 1 << 10
    cirrusBitMask = 1 << 11
    mask = qa.bitwiseAnd(cloudBitMask).eq(0).And(
        qa.bitwiseAnd(cirrusBitMask).eq(0))
    return image.updateMask(mask).divide(10000)

# Loop over weeks
for w in range(num_weeks):
    start = ee.Date.fromYMD(start_date.year, start_date.month, start_date.day).advance(7*w, 'day')
    end = start.advance(7, 'day')
    
    collection = (ee.ImageCollection('COPERNICUS/S2_SR')
                  .filterBounds(himachal)
                  .filterDate(start, end)
                  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 60))
                  .map(maskS2clouds)
                  .select(bands))
    
    composite = collection.median().clip(himachal)
    
    task = ee.batch.Export.image.toDrive(
        image=composite,
        description=f"Himachal_week_{w}",
        folder="himachal_s2_weeks",
        fileNamePrefix=f"S2_week_{w}",
        region=himachal.geometry(),
        scale=10,
        maxPixels=1e13
    )
    task.start()
    print(f"✅ Export started for week {w}: {start.format('YYYY-MM-dd').getInfo()} to {end.format('YYYY-MM-dd').getInfo()}")
