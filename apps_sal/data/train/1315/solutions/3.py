n = int(input())
d = dict()
for i in range(n):
    l = list(map(int, input().split(' ')))
    l1 = []
    l1.append(max(l))
    l1.append(sum(l) - (l1[0] + min(l)))
    l1.append(min(l))
    t = tuple(l1)
    try:
        d[t] += 1
    except:
        d[t] = 0
c = 0
for i in d:
    if(d[i] == 0):
        c += 1
print(c)
