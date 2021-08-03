t = int(input())
ans = []
for i in range(t):
    n = int(input())
    c = 0
    for j in range(n + 1):
        for k in range(0, n - j + 1):
            c += (2**k) * (3**j)
    ans.append(c)
for i in ans:
    print(i)
