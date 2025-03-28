def read_wbd_file2(wbd_filename, huc_level, cache_key,
                  func_key='wbd_08', override=False):
    """
    Read WBD File using cache key.
    
    Args:
        wbd_filename (str): WBD file name 
        huc_level (int): HUC level
        cache_key (str): cache key to `cached` decorator
        func_key (str, optional): File basename used to save pickled results
        override (bool, optional): When True, re-compute even if the results are already stored
    Returns:
        wbd_gdf (gdf): GeoDataFrame
    """
    from landmapy.cached import cached

    @cached(func_key, override)
    def read_wbd_cached(wbd_filename, huc_level, cache_key):
        """
        Internal read WBD File using cache key.
        
        Args:
            wbd_filename (str): WBD file name 
            huc_level (int): HUC level
            cache_key (str): cache key to `cached` decorator
        Returns:
            wbd_gdf (gdf): GeoDataFrame
        """
        import os
        import earthpy as et
        import geopandas as gpd

        print(cache_key)
        # Download and unzip
        wbd_url = (
            "https://prd-tnm.s3.amazonaws.com"
            "/StagedProducts/Hydrography/WBD/HU2/Shape/"
            f"{wbd_filename}.zip")
        wbd_dir = et.data.get_data(url=wbd_url)
                    
        # Read desired data
        wbd_path = os.path.join(wbd_dir, 'Shape', f'WBDHU{huc_level}.shp')
        wbd_gdf = gpd.read_file(wbd_path, engine='pyogrio')
        return wbd_gdf
    
    wbd_gdf = read_wbd_cached(wbd_filename, huc_level, cache_key)
    print(cache_key)
    return wbd_gdf

# read_wbd_file(wbd_filename, huc_level, cache_key)

def read2_delta_gdf(huc_level=12, huc_region='08', watershed='080902030506',
                   dissolve=True,
                   func_key='wbd_08', override=False):
    """
    Read Delta WBD using cache decorator.

    Args:
        huc_level (int): HUC level
        watershed (str): watershed ID
    Return:
        delta_gdf (gdf): gdf of delta
    """
    wbd_gdf = read_wbd_file2(
        f"WBD_{huc_region}_HU2_Shape", huc_level, cache_key=f'hu{huc_level}',
        func_key=func_key, override=override)

    delta_gdf = wbd_gdf[f'huc{huc_level}']
    if not watershed is None:
        delta_gdf = wbd_gdf[delta_gdf.isin([watershed])]
    if dissolve:
        delta_gdf = delta_gdf.dissolve()
#    delta_gdf = (
#        wbd_gdf[wbd_gdf[f'huc{huc_level}']
#        .isin([watershed])]
#        .dissolve()
#    )
    return delta_gdf

# delta_gdf = read_delta_gdf(12)
