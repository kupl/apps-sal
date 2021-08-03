def powers_of_two(n):
    num1 = 0
    list = []
    for x in range(n + 1):
        list.append(pow(2, x))
    return list
