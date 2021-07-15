import math
def dating_range(age):
    if age>14:
        return '-'.join(map(str,[age//2+7,2*(age-7)]))
    return '-'.join(map(str,map(math.floor,[age*0.9,age*1.1])))
