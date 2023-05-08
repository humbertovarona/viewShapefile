shapefile_path = 'data/Shapefile/Brazil/Brasil.shp'
output_path = 'data/Shapefile/Brazil/Brasil.jpeg'

longitude_lim = (-40, -30)
latitude_lim = (-12, -1)

gdf = read_shapefile(shapefile_path)
ax = draw_shapefile(gdf, longitude_lim, latitude_lim)
