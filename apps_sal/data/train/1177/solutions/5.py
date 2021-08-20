t = int(input())
for i in range(t):
    l = input().split()
    n = int(l[0])
    k = int(l[1])
    if n == 0:
        if k == 0:
            print(1)
        else:
            print(0)
    elif k > n:
        print(0)
    else:
        if n - k < k:
            k = n - k
        ans = 1
        for i in range(n - k + 1, n + 1):
            ans *= i
        for i in range(1, k + 1):
            ans /= i
        print(ans)
