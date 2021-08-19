t = int(input())
while t > 0:
    c = input()
    len1 = len(c)
    sum1 = 0
    l = []
    for i in range(len1):
        sum1 += 8
    sum2 = 8
    q = 1
    for i in range(1, len1):
        if c[i] != c[i - 1]:
            if q > 1:
                sum2 += 32
            q = 1
            sum2 += 8
        else:
            q += 1
    if q > 1:
        sum2 += 32
    print(sum1 - sum2)
    t -= 1
