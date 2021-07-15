import math

def dating_range(age):

    if age > 14:
        min = math.floor(age/2 + 7)
        max = (age-7) * 2     
        return '{}-{}'.format(min, max)
    else: 
        min = math.floor(age - 0.10 * age)
        max = math.floor(age + 0.10 * age)
        return '{}-{}'.format(min, max)

