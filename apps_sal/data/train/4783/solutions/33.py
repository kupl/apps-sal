ABOVE_FREEZING_TEMP_MSG = '{} is above freezing temperature'
FREEZING_TEMP_MSG = '{} is freezing temperature'


def weather_info(temp):

    def convert_to_celsius(temperature):
        return (temperature - 32) * (5 / 9)

    result = convert_to_celsius(temp)

    return (ABOVE_FREEZING_TEMP_MSG.format(result)
            if result > 0
            else FREEZING_TEMP_MSG.format(result))
