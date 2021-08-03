t = int(input())
for i in range(0, t):
    n = int(input())
    a = input()
    b = [1] * n
    for i in range(0, n):
        if a[i] == '1':
            b[i] = 0
            if i > 0:
                b[i - 1] = 0
            if i < n - 1:
                b[i + 1] = 0
    ans = 0
    for i in range(0, n):
        if b[i] == 1:
            ans += 1
    print(ans)
