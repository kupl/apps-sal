t = int(input())
for _ in range(t):
    (n, m) = list(map(int, input().split(' ')))
    li = [10 for i in range(n)]
    for j in range(m):
        (s, e, k) = list(map(int, input().split(' ')))
        for i in range(s - 1, e):
            li[i] = li[i] * k
    c = 0
    l = len(li)
    for i in li:
        c += i
    print(int(c / l))
