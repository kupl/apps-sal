def count_by(x, n):
    a = x*n
    s = []
    for i in range(x,a+1):
        if i%x == 0:
            s.append(i)
    return s

