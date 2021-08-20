def weather_info(temp):
    c = (temp - 32) * (5 / 9)
    return '%s is freezing temperature' % c if c < 0 else '%s is above freezing temperature' % c
