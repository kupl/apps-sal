def weather_info(temp):
    cels = (temp - 32) * (5 / 9)
    if cels > 0:
        return f'{cels} is above freezing temperature'
    else:
        return f'{cels} is freezing temperature'
