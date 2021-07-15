def weather_info (temp):
    a=float((temp-32)*(5/9))
    if  a>= 0:   
        return f"{a} is above freezing temperature"
    else:
        return f"{a} is freezing temperature"
