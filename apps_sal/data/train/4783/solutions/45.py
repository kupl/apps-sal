def weather_info(temp_fahrenheit):
    temp_celsius = convert_to_celsius(temp_fahrenheit)
    if (temp_celsius < 0):
        return (str(temp_celsius) + " is freezing temperature")
    else:
        return (str(temp_celsius) + " is above freezing temperature")


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)
