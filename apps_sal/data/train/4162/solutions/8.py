import math

def friends(n):
    if n <= 1:
        return 0
    else:
        return math.ceil(math.log(n) / math.log(2))-1
