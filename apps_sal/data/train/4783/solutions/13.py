def weather_info(temp):
    r = (temp - 32) * (5 / 9)
    return '{} {}'.format(r, ('is freezing temperature', 'is above freezing temperature')[r > 0])
