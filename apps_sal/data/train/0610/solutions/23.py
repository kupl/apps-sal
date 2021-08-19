for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    l = []
    c = 0
    for i in range(n):
        if s[i] == 1:
            l.append(i)
    for i in range(len(l) - 1):
        if l[i + 1] - l[i] < 6:
            c += 1
    if c > 0:
        print('NO')
    else:
        print('YES')
