n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

ans = [0 for i in range(n)]
for cur in range(1, n + 1):
    k = -1
    for i, row in enumerate(a):
        if all((x <= cur for x in row)):
            k = i
            break
    #assert(k != -1)
    for i in range(len(row)):
        row[i] = 999
    ans[k] = cur
print(' '.join(map(str, ans)))
