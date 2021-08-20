def powers_of_two(n):
    arr = []
    for el in range(n + 1):
        arr.append(2 ** el)
    return arr
