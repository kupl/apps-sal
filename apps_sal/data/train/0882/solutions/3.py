T = int(input())
ans = []
for _ in range(T):
    A = input()
    B = input()
    acount = {}
    bcount = {}
    for i in A:
        acount[i] = acount.get(i, 0) + 1
    for i in B:
        bcount[i] = bcount.get(i, 0) + 1
    count = 0
    for i in acount.keys():
        if i in bcount:
            count += min(acount[i], bcount[i])
    ans.append(count)
for i in ans:
    print(i)
