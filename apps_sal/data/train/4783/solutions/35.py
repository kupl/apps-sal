def weather_info(temp):
    temp = (temp - 32) * (5 / 9)
    if temp > 0:
        return str(temp) + ' is above freezing temperature'
    else:
        return str(temp) + ' is freezing temperature'
