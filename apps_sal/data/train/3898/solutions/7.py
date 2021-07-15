def dms(deg, dirs):
    v = abs(deg)
    return (int(v), int(60 * v % 60), 3600 * v % 60, dirs[deg < 0])
def convert_to_dms(dd_lat, dd_lon):
    return '%03d*%02d\'%06.3f"%s' % dms(float(dd_lat), 'NS'), '%03d*%02d\'%06.3f"%s' % dms(float(dd_lon), 'EW')

