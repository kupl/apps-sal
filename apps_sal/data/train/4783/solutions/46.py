def weather_info(temp):
    x = (temp - 32) * (5 / 9)
    if x > 0:
        return str(x) + ' is above freezing temperature'
    elif x < 0:
        return str(x) + ' is freezing temperature'
