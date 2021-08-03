# cook your dish here

t = int(input())
for z in range(t):
    x, r, a, b = list(map(int, input().split()))
    d = abs(a - b)
    if(d == 0):
        print("0")
    else:
        count = 0
        mt = (x * r * 1.0) / max(a, b) * 1.0
        dmt = r * 1.0 / d * 1.0
        ans = int(mt * 1.0 / dmt * 1.0)
        if(ans * dmt * 1.0 == (mt)):
            # print('Test')
            print(int(ans - 1))
        else:
            print(int(ans))
