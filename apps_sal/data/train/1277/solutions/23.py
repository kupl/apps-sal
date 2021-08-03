# cook your dish here
try:
    tap = int(input())
    for i in range(tap):
        num = int(input())
        loss = 0
        for j in range(num):
            l = list(map(int, input().split()))
            p = l[0]
            r = l[1]
            d = l[2]

            t = p + (d / 100) * p
            a = t - t * (d / 100)
            loss += (p - a) * r

        print(loss)
except:
    pass
