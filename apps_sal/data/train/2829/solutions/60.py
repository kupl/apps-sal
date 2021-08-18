def array_madness(a, b):
    result1 = 0
    result2 = 0
    for number in a:
        result1 += number**2
    for number in b:
        result2 += number**3
    if result1 > result2:
        return True
    else:
        return False
