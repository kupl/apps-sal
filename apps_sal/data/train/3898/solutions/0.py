from math import floor


def convert(dd, direction):
    degrees = floor(dd)
    seconds = round(dd % 1 * 3600000)
    return '%03d*%02d\'%06.3f"%s' % (degrees, seconds // 60000, seconds % 60000 / 1000, direction)


def convert_to_dms(dd_lat, dd_lon):
    dd_lat = float(dd_lat)
    dd_lon = float(dd_lon)
    dms_lat = convert(abs(dd_lat), 'N' if dd_lat >= 0 else 'S')
    dms_lon = convert(abs(dd_lon), 'E' if dd_lon >= 0 else 'W')
    return (dms_lat, dms_lon)
