def weather_info(temp):
    temp = convert_to_celsius(temp)
    if temp < 0:
        return f"{temp} is freezing temperature"
    else:
        return f"{temp} is above freezing temperature"


def convert_to_celsius(temperature):
    celsius = (temperature - 32) * (5 / 9)
    return celsius
