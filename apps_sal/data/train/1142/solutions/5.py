n = int(input())
l = []
for i in range(0, n):
    x = int(input())
    l.append(x)
    l.sort(reverse=True)
    print(l.index(x) + 1)
