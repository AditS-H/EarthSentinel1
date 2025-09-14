# Earth Engine Landslide Data Export Notebook

This project provides a Jupyter Notebook for exporting remote sensing indices and terrain data from Google Earth Engine (GEE) for landslide analysis. The notebook is designed to automate the download of NDVI, NDWI, and slope data for a specified region and time period, saving the results to your Google Drive.

## Features
- **Google Earth Engine Authentication**: Handles authentication and initialization for GEE Python API.
- **Region of Interest (ROI) Selection**: Specify a bounding box for your area of interest.
- **Landsat 8/9 Data Processing**: Fetches and processes surface reflectance imagery, applies cloud masking, and computes:
  - NDVI (Normalized Difference Vegetation Index)
  - NDWI (Normalized Difference Water Index)
- **Terrain Analysis**: Extracts slope data from SRTM DEM.
- **Automated Export**: Exports NDVI, NDWI, and slope as GeoTIFFs to Google Drive.

## Requirements
- Python 3.7+
- [earthengine-api](https://developers.google.com/earth-engine/guides/python_install)
- [geemap](https://geemap.org/)
- Google account with access to [Google Earth Engine](https://signup.earthengine.google.com/)

## Setup
1. **Install dependencies**:
   ```bash
   pip install earthengine-api geemap
   ```
2. **Authenticate with Google Earth Engine**:
   - The notebook will prompt you to authenticate on first run.

## Usage
1. Open `first.ipynb` in Jupyter or VS Code.
2. Run the first cell to authenticate and initialize Earth Engine.
3. Use the `process_indices` function:
   - Provide your ROI bounds, start date, and end date.
   - Example:
     ```python
     roi_bounds = [-122.0, 37.0, -121.0, 38.0]  # [xmin, ymin, xmax, ymax]
     start_date = '2022-01-01'
     end_date = '2022-12-31'
     process_indices(roi_bounds, start_date, end_date)
     ```
4. Download the exported GeoTIFFs from your Google Drive folder (default: `LandslideData`).

## Notes
- Cloud masking is applied for cleaner composites.
- Slope is static (from SRTM DEM) and not date-dependent.
- Monitor export tasks in the Earth Engine Code Editor or with `ee.batch.Task.list()`.

## License
This project is for academic and research purposes. See the repository for license details.
