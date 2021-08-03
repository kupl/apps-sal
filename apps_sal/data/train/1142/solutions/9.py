t = int(input())
l = []
for _ in range(t):
    n = int(input())
    l.append(n)
    l.sort(reverse=True)
    print(l.index(n) + 1)
