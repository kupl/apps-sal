for _ in range(int(input())):
    n, r = map(int, input().split())
    s = []
    d = dict()
    for i in range(r):
        a, b = map(str, input().split())
        s.append([int(b), a])
        a = list(a)
        a.sort()
        d[''.join(a)] = i
    for i in range(n - r):
        a, b = map(str, input().split())
        a = list(a)
        a.sort()
        s[d[''.join(a)]][0] += int(b)
    s.sort(key=lambda x: x[1], reverse=True)
    s.sort(key=lambda x: x[0])
    for i in range(-1, -r - 1, -1):
        print(s[i][1], s[i][0])
