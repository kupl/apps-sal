def weather_info(temp):
    c = convert_to_celsius(temp)
    if (c > 0):
        return ("{} is above freezing temperature").format(c)
    else:
        return ("{} is freezing temperature").format(c)


def convert_to_celsius(temperature):
    var_celsius = (temperature - 32) * (5 / 9)
    var_celsius = float(var_celsius)
    return var_celsius
