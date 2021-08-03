def powers_of_two(n):
    i = 0
    s = 1
    array = []
    while i <= n:
        array.append(s)
        i += 1
        s = (2 ** i)
    return array
