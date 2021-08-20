def convert_to_dms(dd_lat, dd_lon):
    (dd_lat, dd_lon) = (float(dd_lat), float(dd_lon))
    if dd_lat >= 0:
        lat_dir = 'N'
    else:
        lat_dir = 'S'
        dd_lat *= -1
    lat_d = int(dd_lat)
    lat_m = (dd_lat - lat_d) * 60
    lat_s = round((lat_m - int(lat_m)) * 60, 3)
    lat_m = int(lat_m)
    dms_lat = '{:03d}*{:02d}\'{:06.3f}"{}'.format(lat_d, lat_m, lat_s, lat_dir)
    if dd_lon >= 0:
        lon_dir = 'E'
    else:
        lon_dir = 'W'
        dd_lon *= -1
    lon_d = int(dd_lon)
    lon_m = (dd_lon - lon_d) * 60
    lon_s = round((lon_m - int(lon_m)) * 60, 3)
    lon_m = int(lon_m)
    dms_lon = '{:03d}*{:02d}\'{:06.3f}"{}'.format(lon_d, lon_m, lon_s, lon_dir)
    return (dms_lat, dms_lon)
