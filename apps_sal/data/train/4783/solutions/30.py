def weather_info(temp):
    temp1 = (temp - 32) * (5 / 9)
    if temp1 > 0:
        return '{} is above freezing temperature'.format(temp1)
    else:
        return '{} is freezing temperature'.format(temp1)
