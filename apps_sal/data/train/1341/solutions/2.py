t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    e = n - 1
    for i in range(n - 2, -1, -1):
        if a[i + 1] > a[i]:
            e = i
        else:
            break
    cnt = 0
    for i in range(n):
        if i - 2 >= 0 and a[i - 2] >= a[i - 1]:
            break
        if e <= i:
            e = i + 1
        while e < n and i - 1 >= 0 and a[i - 1] >= a[e]:
            e += 1
        cnt += n - e + 1
    print(cnt - 1)
