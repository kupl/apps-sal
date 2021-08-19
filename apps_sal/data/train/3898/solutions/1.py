def convert_to_dms(dd_lat, dd_lon):

    def convert(dd, c):
        d = abs(dd)
        m = d % 1 * 60
        s = m % 1 * 60
        return '{:03}*{:02}\'{:06.3f}"{}'.format(int(d), int(m), s, c[dd >= 0])
    return (convert(float(dd_lat), 'SN'), convert(float(dd_lon), 'WE'))
