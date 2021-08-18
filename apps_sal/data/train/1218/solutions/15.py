t = int(input())
for _ in range(t):
    x, n = map(int, input().split())
    a = []
    for i in range(1, n):
        if i % x == 0:
            a.append(i)
    print(sum(a))
