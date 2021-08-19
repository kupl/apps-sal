def weather_info(temp):
    c = convert_to_celsius(temp)
    result = f'{c} is above freezing temperature'
    result2 = f'{c} is freezing temperature'
    if c > 0:
        return result
    else:
        return result2


def convert_to_celsius(temperature):
    celsius = (temperature - 32.0) * (5.0 / 9.0)
    return celsius
