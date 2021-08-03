def weather_info(temp):
    c = convertToCelsius(temp)
    return '{} {}'.format(c, 'is freezing temperature' if c < 0 else 'is above freezing temperature')


def convertToCelsius(temp):
    return (temp - 32) * 5 / 9.0
