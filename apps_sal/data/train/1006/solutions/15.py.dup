t = int(input())

while t:
    n, d = [int(x) for x in input().split()]

    ans = 0
    if n == 1:
        ans = d if n > d else n
        print(ans)
    else:
        temp = str(n)
        l = len(temp)
        orig = temp[l - 1]
        if int(orig) > d:
            updat = str(d)
        else:
            updat = orig

        orig = updat

        for i in range(l - 2, -1, -1):
            orig = temp[i] + updat
            updat = updat + str(d)
            if int(orig) > int(updat):
                orig = updat
            else:
                updat = orig

        print(int(orig))
    t -= 1
