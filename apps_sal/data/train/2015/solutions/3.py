n = int(input())
kids = []
for i in range(1, n + 1):
    kids.append([int(x) for x in input().split()] + [i])
kids.reverse()
ans = []
while kids:
    v, d, p, k = kids.pop()
    ans.append(k)
    for i in range(max(-v, -len(kids)), 0):
        kids[i][2] -= v + i + 1
    for i in range(len(kids) - 1, -1, -1):
        if kids[i][2] < 0:
            for j in range(i):
                kids[j][2] -= kids[i][1]
            kids.pop(i)
print(len(ans))
for kid in ans:
    print(kid, end=' ')
