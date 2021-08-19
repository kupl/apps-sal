def weather_info(temp):
    celsius = (temp - 32) * (5 / 9)
    if celsius < 0:
        return f'{celsius} is freezing temperature'
    else:
        return f'{celsius} is above freezing temperature'
