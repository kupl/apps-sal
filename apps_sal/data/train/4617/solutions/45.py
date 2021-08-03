def powers_of_two(n):
    ls = []
    i = 0
    while i <= n:
        ls.append(2**i)
        i = i + 1
    return ls
