n = int(input())
if n > 999999999 or n < -999999999:
    print(0)
else:
    n += 1
    f = False
    p = False
    while n <= 987654321:
        k = str(n)
        if k.count('0') == 0:
            for i in range(len(k)):
                if k.count(k[i]) > 1:
                    p = True
                    break
            if p:
                p = False
            else:
                f = True
                break

        n += 1
    if f:
        print(n)
    else:
        print(0)
