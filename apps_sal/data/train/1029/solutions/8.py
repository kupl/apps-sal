t = int(input())
for _ in range(t):
    (a, b) = map(int, input().split())
    c = [int(i) for i in input().split()]
    d = [int(i) for i in range(1, a + 1)]
    d = list(set(d) - set(c))
    d.sort()
    j = 0
    while j < len(d):
        print(d[j], end=' ')
        j += 2
    j = 1
    print()
    while j < len(d):
        print(d[j], end=' ')
        j += 2
    print()
