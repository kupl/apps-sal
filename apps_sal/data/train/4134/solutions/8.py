import math


def cooking_time(needed_power, minutes, seconds, power):
    in_seconds = 60 * minutes + seconds
    increase = int(needed_power[:-1]) / int(power[:-1])
    new_seconds = in_seconds * increase
    output_minutes = int(new_seconds / 60)
    output_seconds = new_seconds % 60
    if math.ceil(output_seconds) == 60:
        output_seconds = 0
        output_minutes += 1
    return str(math.ceil(output_minutes)) + ' minutes ' + str(math.ceil(output_seconds)) + ' seconds'
