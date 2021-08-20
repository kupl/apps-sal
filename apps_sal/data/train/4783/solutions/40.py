def weather_info(temperature):
    c = convert_to_celsius(temperature)
    if c > 0:
        return f'{c} is above freezing temperature'
    else:
        return f'{c} is freezing temperature'


def convert_to_celsius(temperature):
    c = (temperature - 32) * (5 / 9)
    return c
