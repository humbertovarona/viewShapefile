import geopandas as gpd
import matplotlib.pyplot as plt

def read_shapefile(shapefile_path):
    gdf = gpd.read_file(shapefile_path)
    return gdf

def draw_shapefile(gdf, lonlim, latlim):
    ax = gdf.plot(facecolor='#CDC0B0', edgecolor='black', linewidth=0.5, figsize=(12, 8))
    ax.set_xlim(lonlim)
    ax.set_ylim(latlim)
    plt.grid()
    plt.title('Shapefile Plot')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.savefig(output_path, dpi=500)
    plt.show()
    return ax
  
  
