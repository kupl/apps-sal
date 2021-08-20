def weather_info(temp):
    c = (temp - 32) * (5.0 / 9)
    if c > 0:
        return str(c) + ' is above freezing temperature'
    else:
        return str(c) + ' is freezing temperature'
