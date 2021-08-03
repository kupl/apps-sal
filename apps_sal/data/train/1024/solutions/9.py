
t = int(input())
grandsum = 0
while t:
    l = list(map(int, input().strip().split()))
    s = l[0]
    n = l[1]
    k = l[2]
    r = l[3]
    res = k

    for i in range(1, n):
        k = k * r
        res = res + k
    if res <= s:
        print("POSSIBLE", str(s - res))
        grandsum += (s - res)
    else:
        print("IMPOSSIBLE", str(abs(s - res)))
        grandsum -= abs(s - res)

    t -= 1
if grandsum < 0:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
