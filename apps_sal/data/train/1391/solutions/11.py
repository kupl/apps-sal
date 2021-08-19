from sys import stdin
for _ in range(int(input())):
    (n, k) = map(int, input().split())
    lst = []
    cmpmt = {}
    cnt = 0
    for i in range(n):
        (si, fi, pi) = map(int, stdin.readline().split())
        lst.append((fi, si, pi))
    lst = sorted(lst)
    for i in lst:
        if i[2] not in cmpmt:
            cmpmt[i[2]] = i[0]
            cnt += 1
        elif cmpmt[i[2]] <= i[1]:
            cmpmt[i[2]] = i[0]
            cnt += 1
    print(cnt)
