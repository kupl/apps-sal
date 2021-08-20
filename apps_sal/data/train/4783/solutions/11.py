def weather_info(temp):
    c = (temp - 32) * (5 / 9)
    if c < 0:
        return f'{c} is freezing temperature'
    else:
        return f'{c} is above freezing temperature'
