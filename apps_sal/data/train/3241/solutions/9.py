def buy_newspaper(s1,s2):
    a = []
    for i in s2:
        try:
            a += [s1.index(i)]
        except:
            return -1
    c = 1
    for i in range(len(a)-1):
        if a[i+1] <= a[i]:
            c += 1
    return c
