t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    t = 0
    for i in range(n - 1, 0, -1):
        if a[i] > a[i - 1]:
            t = i
            break
        if i == 1:
            t = 0
    if t <= 1:
        print(0)
        continue
    s = 0
    for i in range(t, 0, -1):
        if a[i] < a[i - 1]:
            s = i
            break
        if i == 1:
            s = 0
    print(s)
