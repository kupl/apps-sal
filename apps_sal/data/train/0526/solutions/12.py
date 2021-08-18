t = int(input())
while t > 0:
    c = input()
    len1 = len(c)
    sum1 = 0
    l = []
    for i in range(len1):
        if c[i].isalpha():
            sum1 += 8
        else:
            sum1 += 32
    sum2 = 0
    l.append(c[0])
    q = 1
    for i in range(1, len1):
        if c[i].isalpha():
            if c[i] == c[i - 1]:
                q += 1
            else:
                if q > 1:
                    l.append(q)
                l.append(c[i])
                q = 1
        else:
            if q > 1:
                l.append(q)
            q = 1
            l.append(c[i])
    if c[len1 - 1].isalpha():
        if q > 1:
            l.append(q)
    for i in l:
        if str(i).isalpha():
            sum2 += 8
        else:
            sum2 += 32
    print(sum1 - sum2)
    t -= 1
