def x(n):
    res = ''
    for i in range(n):
        t = ''
        for j in range(n):
            t += '■' if j == i or j == n-1-i else '□'
        res += t+'\n'
    return res[:len(res)-1]
