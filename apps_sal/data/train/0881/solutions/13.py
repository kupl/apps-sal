t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    c = [1] * n
    for i in range(n - 1):
        if l[i] <= l[i + 1]:
            c[i + 1] = c[i] + 1
    print(sum(c))
