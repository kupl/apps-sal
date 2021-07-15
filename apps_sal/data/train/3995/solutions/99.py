from math import floor
def dating_range(age):
    if age > 14:
        min = age/2 + 7 
        max = (age -7)*2
    else:
        min = floor(age - 0.10*age)
        max = floor(age + 0.10*age)
    return str(floor(min)) + '-' + str(floor(max))
