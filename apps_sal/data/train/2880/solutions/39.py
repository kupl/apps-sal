def seven(m):
    i = 0
    while m>=100 or (m%7 and m>=100):
        i, m = i+1, int(str(m)[:-1])-2*int(str(m)[-1])
    return m, i
