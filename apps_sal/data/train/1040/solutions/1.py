from bisect import bisect_left
for _ in range(int(input())):
    (n, q) = map(int, input().split())
    s = input()
    l = []
    for i in range(n - 2):
        (a, b, c) = (s[i], s[i + 1], s[i + 2])
        if len(set([a, b, c])) < 3:
            l.append(i)
    for i in range(q):
        (left, right) = map(int, input().split())
        left -= 1
        right -= 1
        if right - left + 1 < 3:
            print('NO')
            continue
        p1 = bisect_left(l, left)
        if p1 != len(l) and l[p1] <= right - 2:
            print('YES')
        else:
            print('NO')
