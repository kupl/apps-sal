(n, k2) = map(int, input().split())

l = []
for i in range(n):
    t = input().split()
    t = [int(x) for x in t]
    l.append([])
    l[i] = t[1:]
# print(l)

total = 1
ans = set(l[0])
notPres = []
for i in l[1:]:
    count = 0
    temp = []
    for j in i:
        if j in ans:
            count += 1
    if count >= k2:
        total += 1
        for j in i:
            ans.add(j)
        index = []
        indC = 0
        for k in notPres:
            c = 0
            for l in k:
                if l in ans:
                    c += 1
            if c >= k2:
                total += 1
                for l in k:
                    ans.add(l)
                index.append(indC)
            indC += 1
        for i in index:
            notPres[i] = []
    else:
        notPres.append(i)
for i in notPres:
    c = 0
    for l in i:
        if l in ans:
            c += 1
            if c >= k2:
                total += 1
                for l in k:
                    ans.add(l)
    # print(notPres)
print(total)
