def weather_info (temp):
    res = (temp-32)*(5/9)
    if(res>0):
        return str(res)+' is above freezing temperature'
    else:
        return str(res)+' is freezing temperature'
