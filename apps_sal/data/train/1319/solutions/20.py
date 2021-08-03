[n, m] = list(map(int, input().split()))
l = []
for _ in range(n + m):
    t = int(input())
    if t == -1:
        print(max(l))
        l.remove(max(l))
    else:
        l.append(t)
