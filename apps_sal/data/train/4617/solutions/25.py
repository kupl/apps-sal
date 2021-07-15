def powers_of_two(n):
    emptylist = []
    for num in list(range(n+1)):
        x = 2**num
        emptylist.append(x)
    return emptylist
