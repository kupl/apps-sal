
t = int(input())
for _ in range(t):
    n, c = list(map(int, input().split()))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    temp = {}
    group = {}
    for i in range(n):
        if arr[i][0] - arr[i][1] not in temp:
            temp[arr[i][0] - arr[i][1]] = [arr[i][0]]
        else:
            temp[arr[i][0] - arr[i][1]].append(arr[i][0])
    noc = 0
    nop = 0
    for d in temp:
        for x in temp[d]:
            if x % c not in group:
                group[x % c] = [x]
            else:
                group[x % c].append(x)
        for e in group:
            noc += 1
            grp = sorted(group[e])
            med = grp[int(len(grp) / 2)]
            for i in range(len(grp)):
                nop += abs(grp[i] - med) // c
        group.clear()
    print(noc, nop)
