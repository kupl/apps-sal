# cook your dish here
while True:
    try:
        n = int(input())
        lis = []
        for i in range(n):
            k = list(map(int, input().split()))
            k.append(k[1] + k[2])
            lis.append(k)

        # print(lis)
        p = sorted(lis, key=lambda x: x[3], reverse=True)
        # print(p)
        maxi = 0
        s = 0
        w = 0
        for i in range(n):
            s += p[i][0]
            w = s + p[i][1] + p[i][2]
            maxi = max(maxi, w)

        print(maxi)

    except:
        break
