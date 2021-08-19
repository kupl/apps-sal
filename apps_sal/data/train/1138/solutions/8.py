t = eval(input())
for _ in range(t):
    n = eval(input())
    a = [int(x) for x in input().strip().split()]
    ca = []
    ans = 0
    for (i, v) in enumerate(a):
        if v == 0:
            ans += 0
            ca = [i + 1] + ca
        else:
            posOfTarget = ca.index(v) + 1
            leftOfTarget = posOfTarget
            rightOfTarget = len(ca) - posOfTarget
            ans += min(leftOfTarget, rightOfTarget)
            ca = ca[:posOfTarget] + [i + 1] + ca[posOfTarget:]
    print(ans)
