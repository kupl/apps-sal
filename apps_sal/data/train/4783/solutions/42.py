def weather_info(temp):
    c = 5 / 9 * (temp - 32)
    if (c < 0):
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")
