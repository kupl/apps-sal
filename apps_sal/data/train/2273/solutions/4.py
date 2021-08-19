from sys import stdin
input = stdin.readline
q = int(input())
for _ in range(q):
    n = int(input())
    l = list(map(int, input().split()))
    cyk = [(i + l[i]) % n for i in range(n)]
    cyk.sort()
    dupa = 1
    for i in range(1, n):
        if cyk[i] != cyk[i - 1] + 1:
            dupa = 0
    if dupa:
        print('YES')
    else:
        print('NO')
