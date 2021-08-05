T = int(input())
for i in range(T):
    n, m = list(map(int, input().split()))
    if(m <= 2):
        print("impossible")
    else:
        l = [0] * m

        if(m % 2 == 0):
            a = m // 2
        else:
            a = (m // 2) + 1
        for j in range(a):
            if(j % 2 == 0):
                l[j] = "a"
                l[m - j - 1] = "a"

            else:
                l[j] = "b"
                l[m - j - 1] = "b"

        r = ""
        s = n // m
        for e in l:
            r = r + e
        print(r * s)
