mod = 10**9 + 7
n = eval(input())
arr = list(map(int, input().strip().split()))
for _ in range(eval(input())):
    q = list(map(int, input().strip().split()))
    if q[0] == 1:
        p, f = q[1], q[2]
        arr[p - 1] = f
    else:
        r = q[1]
        ans = 1
        for i in range(0, n, r):
            ans *= arr[i]
            ans = ans % mod
        print(str(ans)[0], ans % mod)
