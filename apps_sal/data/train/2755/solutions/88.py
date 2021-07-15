def multiple_of_index(arr):
    n_arr = []
    a1 = tuple(arr)
    n = 0
    m = 0
    for i in range(len(a1)):
        n = i
        m = a1[i]
        if n == 0:
                continue
        elif m % n == 0:
            n_arr.append(m)
            
    return n_arr
