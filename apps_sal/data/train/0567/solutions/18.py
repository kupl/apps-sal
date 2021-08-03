t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    x = [0] * n
    for i in range(n - 2):
        x[i] = x[i + 1] = x[i + 2] = l[i]
    for j in range(n - 1, 1, -1):
        if l[j] != x[j]:
            x[j] = x[j - 1] = x[j - 2] = l[j]

    if x == l:
        print('Yes')
    else:
        print('No')
