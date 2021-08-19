def weather_info(temp_fahrenheit):
    temp_celsius = convert_to_celsius(temp_fahrenheit)
    return f'{temp_celsius} is freezing temperature' if temp_celsius < 0 else f'{temp_celsius} is above freezing temperature'


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)
