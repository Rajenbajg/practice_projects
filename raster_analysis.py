import pandas as pd
import numpy as np
import rasterio

def tif_to_dataframe(file_path):
    # Open TIF file using rasterio
    with rasterio.open(file_path) as src:
        # Read data and geospatial information
        data = src.read()
        transform = src.transform
        crs = src.crs
    
    # Get pixel coordinates for each pixel in the image
    nrows, ncols = data.shape[1:]
    row, col = np.meshgrid(np.arange(nrows), np.arange(ncols), indexing='ij')
    
    # Convert pixel coordinates to geospatial coordinates
    lon, lat = transform * (col.flatten(), row.flatten())
    
    # Create pandas DataFrame with latitude, longitude, and pixel value
    df = pd.DataFrame({
        'lat': lat,
        'lon': lon,
        'value': data.flatten()
    })
    # Set CRS of DataFrame
    df.crs = crs
    
    return df

df_pd =tif_to_dataframe('C:/Users/rajen/Desktop/outage_probability_veg_augmented.tif')
#print(df_pd)

subset_df = df_pd.loc[df_pd.value != -9999.0]
print(subset_df)
