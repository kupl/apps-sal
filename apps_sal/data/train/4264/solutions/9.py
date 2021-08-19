def operation(a, b):
    count = 0
    while a != b:
        while a != 1 and a & a - 1:
            a //= 2
            count += 1
        if a < b:
            a *= 2
            count += 1
        elif a > b:
            a //= 2
            count += 1
    return count
