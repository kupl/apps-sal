def weather_info (t):
    c = convert(t)
    if (c > 0):
        return (str(c) + " is above freezing temperature")
    else:
        return (str(c) + " is freezing temperature")
def convert(t):
    cs = (t - 32) * (5/9)
    return cs
