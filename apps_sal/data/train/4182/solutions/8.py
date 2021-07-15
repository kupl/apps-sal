import math
def survivor(n):
    lst = [1, 3, 7, 13, 19, 27, 39, 49, 67, 79]
    if n < 80:
        return False if n not in lst else True
    for i in range(2, n):
        if n-1 < i:
            break
        if n % i == 0:
            return False
        n = n-math.ceil(n//i)
    return True
