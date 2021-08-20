from bisect import bisect_left as bl
t = int(input())
for i in range(t):
    (n, q) = map(int, input().split())
    s = input()
    c = []
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i + 1] == s[i + 2] or s[i] == s[i + 2]:
            c.append(i + 1)
    for i in range(q):
        (l, r) = map(int, input().split())
        x = bl(c, l)
        if len(c) == 0 or r - l < 2 or x == len(c):
            print('NO')
        else:
            st = c[x]
            if st + 2 <= r:
                print('YES')
            else:
                print('NO')
