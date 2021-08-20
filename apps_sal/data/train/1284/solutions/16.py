t = int(input())
for j in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    a = n // 4
    b = 2 * a
    c = 3 * a
    if l[a] == l[a - 1] or l[b - 1] == l[b] or l[c] == l[c - 1]:
        print('-1')
    else:
        print(l[a], l[b], l[c])
