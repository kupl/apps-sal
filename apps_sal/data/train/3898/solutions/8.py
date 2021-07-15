def f(l,d):
    a= abs(l)
    a1=int(a)
    a=60*(a-a1)
    a2=int(a)
    a=round(60*(a-a2),3)
    return '{:03}*{:02}\'{:06.3f}"{}'.format(a1,a2,a,d)

def convert_to_dms(lat, lon):
    a = float(lat)
    ns = ["S","N"][a>=0]
    b = float(lon)
    we = ["W","E"][b>=0]
    return f(a,ns), f(b,we)
