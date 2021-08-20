def weather_info(temp):
    c = round((temp - 32) * (5 / 9), 16)
    return f'{c} is above freezing temperature' if c > 0 else f'{c} is freezing temperature'
