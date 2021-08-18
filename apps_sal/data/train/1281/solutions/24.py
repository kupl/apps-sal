t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    c = []
    for i in l:
        if i not in c:
            c.append(i)
    c.sort()
    print('yes' if (c == [1, 2, 3, 4, 5, 6, 7] and l == l[::-1]) else 'no')
