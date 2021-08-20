t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    c = 0
    s = 0
    for i in range(n):
        if s + k < a[i]:
            while s + k < a[i]:
                s += k
                c += 1
        s = a[i]
    print(c)
