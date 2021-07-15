from math import floor

def deg_min_sec(coord):
    
    deg = floor(abs(float(coord)))
    
    min = floor((abs(float(coord)) - deg)*60)
    
    sec = floor((abs(float(coord)) - deg - min/60)*3600)
    
    dec = str(round((abs(float(coord)) - deg - min/60)*3600 - sec, 3))[2:]
                
    return f'{deg:03}*{min:02}\'{sec:02}.{dec:<03}"'

def convert_to_dms(dd_lat, dd_lon):
      
    lat_card = 'S' if '-' in str(dd_lat) else 'N'
    
    lon_card = 'W' if '-' in str(dd_lon) else 'E'
       
    return f'{deg_min_sec(dd_lat)}{lat_card}', f'{deg_min_sec(dd_lon)}{lon_card}'

