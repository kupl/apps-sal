def multiple_of_index(arr):
    x = []
    for idx, n in enumerate(arr):
        if idx >= 1 and n % idx == 0:
            x.append(n)
    return x
