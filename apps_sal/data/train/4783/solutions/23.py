
def convert_to_celsius(temp):
    celsius = (temp - 32) * (5 / 9)
    return celsius


def weather_info(temp):
    x = convert_to_celsius(temp)
    if (x > 0):
        return f"{x} is above freezing temperature"
    else:
        return f"{x} is freezing temperature"
