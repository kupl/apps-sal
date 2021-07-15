import math
def friends(n):
    print(n)
    if n <= 2:
        return 0
    elif math.log(n,2)==int(math.log(n,2)):
        return int(math.log(n,2)) -1
    else:
        return int(math.log(n,2))

