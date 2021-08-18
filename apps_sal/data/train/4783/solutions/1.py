def weather_info(t):
    c = (t - 32) * (5.0 / 9)
    return str(c) + " is freezing temperature" if c <= 0 else str(c) + " is above freezing temperature"
