import math
def reverse(hernia):
    power = int(math.log10(hernia))
    if power == 0:
        return hernia
    else:
        return ((hernia % 10) * (10 ** power)) + reverse(hernia // 10)
