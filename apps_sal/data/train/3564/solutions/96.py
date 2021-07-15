import math
def stringy(size):
    if size == 1:
        return '1'
    elif size%2 == 0:
        return '10'*int((size/2))
    else:
        return '10'*(math.floor(size/2)) + '1'
