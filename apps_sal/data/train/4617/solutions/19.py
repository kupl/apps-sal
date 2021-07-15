def powers_of_two(n):
    list_n = []
    i = 0
    while i != n + 1:
        list_n.append(2 ** i)
        i += 1   
    return list_n
