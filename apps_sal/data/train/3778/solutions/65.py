def find_smallest_int(a):
    M = 1000000000000
    for i in range(len(a)):
        if a[i] < M:
            M = a[i]
    return M

