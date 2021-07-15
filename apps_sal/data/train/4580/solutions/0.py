def tiaosheng(a):
    j, t = 0, 0
    for j in a:
        t += 3
        if j + t > 60:
            return min(j, 60-t+3)
    return 60-t
