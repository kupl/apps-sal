def array_madness(a,b):
    sum = 0
    sumc = 0
    for i in a:
        sum += (i ** 2)
    for i in b:
        sumc += (i ** 3)
    if sum > sumc:
        return True
    else:
        return False
