def count_sheep(n):
    s = ""
    i = 1
    for i in range(1, n + 1):
        s += (str(i) + " sheep...")

    return s
