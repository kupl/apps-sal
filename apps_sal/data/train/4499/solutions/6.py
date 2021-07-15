
def convergents_of_e(n):
    
    n0, n1, L = 1, 2, n
    for i in range(2, n + 1):
        if i % 3 != 0:
            m = 1
        else:
            m = 2 * i // 3
        n0, n1 = n1, n0 + n1 * m
    return sum((int(i) for i in str(n1)))
