t = int(input())
for i in range(t):
    n = int(input())
    x = [1]
    for i in range(1, n):
        p = (i**2 + (i + 1)**3) % 1000000007
        x.append(p)
    print(x[n - 1])
