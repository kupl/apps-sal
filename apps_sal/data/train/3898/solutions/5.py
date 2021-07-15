def convert_to_dms(dd_lat, dd_lon):
    def dd_to_dms(dd):
        h=int(dd);dd-=h
        m=int(dd*60);dd-=m/60
        s=round(dd*3600,3)
        return (h,m,s)
    dd_lat,dd_lon=map(float,(dd_lat,dd_lon))
    dms_lat="{:03d}*{:02d}\'{:06.3f}\"{:s}".format(*dd_to_dms(abs(dd_lat)),"NS"[dd_lat<0])
    dms_lon="{:03d}*{:02d}\'{:06.3f}\"{:s}".format(*dd_to_dms(abs(dd_lon)),"EW"[dd_lon<0])
    return (dms_lat,dms_lon)
