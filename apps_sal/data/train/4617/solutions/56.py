def powers_of_two(n):
    powof2 = []
    num = 1
    for i in range(n + 1):
        powof2.append(num)
        num *= 2
    return powof2
