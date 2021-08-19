# cook your dish here
t = int(input())
extra = 0
required = 0
while t > 0:
    s, n, k, r = list(map(int, input().split()))
    sum1 = k
    pro = k
    for i in range(1, n):
        pro = pro * r
        sum1 += pro
    z = s - sum1
    if z >= 0:
        extra += z
        print("POSSIBLE", z)
    else:
        z = z * (-1)
        required += z
        print("IMPOSSIBLE", z)
    t -= 1
if extra - required >= 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
