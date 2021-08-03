
def weather_info(c):

    c = ((c) - 32) * (5 / 9)

    if c < 0:
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")
