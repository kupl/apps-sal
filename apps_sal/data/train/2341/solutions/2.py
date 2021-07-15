t = int(input())
for _ in range(t):
    n, m, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    ans = 0
    control_forward = min(k, m-1)
    for i in range(control_forward+1):
        l = i
        r = n-1-control_forward+i
        non_control_forward = max(m-1-control_forward, 0)
        anstemp = 10**10
        for j in range(non_control_forward+1):
            l += j
            r += -non_control_forward + j
            anstemp = min(anstemp, max(a[l], a[r]))

            l -= j
            r -= -non_control_forward + j
        ans = max(anstemp, ans)

    print(ans)

