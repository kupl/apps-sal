def gms(x):
    c = x >= 0
    x = abs(x)
    g = int(x)
    x = 60 * (x - g)
    m = int(x)
    x = 60 * (x - m)
    s = round(x, 3)
    return (g, m, s, c)


def formatea(g, m, s, c):
    g = '{:03d}'.format(g)
    m = '{:02d}'.format(m)
    s = '{:02.3f}'.format(s)
    s = '0' * (6 - len(s)) + s
    return f'''{g}*{m}'{s}"{c}'''


def convert_to_dms(*args):
    (dd_lat, dd_lon) = map(float, args)
    dms_lat = gms(dd_lat)
    dms_lon = gms(dd_lon)
    a = formatea(*dms_lat[:3], 'N' if dms_lat[3] else 'S')
    b = formatea(*dms_lon[:3], 'E' if dms_lon[3] else 'W')
    return (a, b)
