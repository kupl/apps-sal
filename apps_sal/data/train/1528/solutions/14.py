t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    li = list(input().split())
    h = li.count('H')
    t = n - h
    for i in range(k):
        d = li[-1]
        li = li[:-1]
        if d == 'T':
            t = t - 1
        else:
            h, t = t, h - 1
            li = ['H' if li[j] == 'T' else 'T' for j in range(n - i - 1)]
    print(h)
