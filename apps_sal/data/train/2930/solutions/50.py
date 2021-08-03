def summation(num):
    a = 1
    num = num + 1
    for x in range(1, num):
        if x < num:
            a = a + x
    return a - 1
