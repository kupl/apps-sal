def powers_of_two(n):
    new_arr = []
    for i in range(n+1):
        new_arr.append(2 ** i)
    return new_arr
