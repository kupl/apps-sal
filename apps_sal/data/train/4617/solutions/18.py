def powers_of_two(n):
    a = 0
    arr = []
    while a <= n:
        arr.append(2 ** a)
        a += 1
    return arr
