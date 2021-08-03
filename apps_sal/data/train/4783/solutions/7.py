def weather_info(temp):
    celsius = (temp - 32) * (5 / 9)
    if celsius > 0:
        return '%s is above freezing temperature' % celsius
    elif celsius < 0:
        return '%s is freezing temperature' % celsius
