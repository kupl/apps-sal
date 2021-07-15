def weather_info (temp):
    c = (temp - 32.0) * 5/9
    if (c < 0):
        return ("{} is freezing temperature".format(c))
    else:
        return ("{} is above freezing temperature".format(c))
