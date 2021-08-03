P, S = list(map(int, input().split()))
ans = []
for index in range(P):
    SC = list(map(int, input().split()))
    NS = list(map(int, input().split()))
    mlist = []
    for i in zip(SC, NS):
        mlist.append(i)
    mlist = sorted(mlist, key=lambda z: (z[0], z[1]), reverse=False)

    counter = 0
    for i in range(1, len(mlist)):
        if mlist[i - 1][1] > mlist[i][1]:
            counter += 1
    ans.append((counter, index + 1))

ans = sorted(ans, key=lambda v: v[0], reverse=False)
for i in ans:
    print(i[1])
