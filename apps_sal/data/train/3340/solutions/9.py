def sharkovsky(a, b):
    i = 0
    while a % 2 == 0:
        a //= 2
        i += 1
    j = 0
    while b % 2 == 0:
        b //= 2
        j += 1
    if a == 1 and b == 1:
        return i > j
    elif a == 1:
        return False
    elif b == 1:
        return True
    elif i == j:
        return a < b
    else:
        return i < j
