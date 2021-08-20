t = int(input())
while t > 0:
    val = str(input()).split(' ')
    n = int(val[0])
    k = int(val[1])
    l = int(val[2])
    if n > k * l or (n > 1 and k == 1):
        print(-1)
    else:
        i = 1
        for a in range(n):
            if i > k:
                i = 1
            print(i, end=' ')
            i += 1
        print()
    t -= 1
