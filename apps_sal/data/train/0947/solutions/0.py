def codn1(s1, s2, p):
    c = 0
    ind = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            c += 1
            ind = i
    if c > 1 or ind == len(s1) - 1:
        return 0
    if s1[ind] > s2[ind] and s1[ind] in s2[ind + 1:]:
        p[0] = True
    if s1[ind] < s2[ind] and s2[ind] in s1[ind + 1:]:
        p[1] = True
    return 1


def codn2(s1, s2):
    if len(s1) < len(s2):
        for i in range(len(s2)):
            if s2[:i] + s2[i + 1:] == s1:
                return 1
    else:
        for i in range(len(s1)):
            if s1[:i] + s1[i + 1:] == s2:
                return 2


def longest(k):
    if cost[k] > 0:
        return cost[k]
    for i in list(d[k]):
        cost[k] = max(cost[k], longest(i) + 1)
    return cost[k]


n = int(input())
l = []
d = {}
cost = {}
for i in range(n):
    l.append(input())
    d[i] = []
    cost[i] = 0
for i in range(n):
    for j in range(n):
        if i != j:
            p = [False, False]
            if len(l[i]) == len(l[j]):
                if codn1(l[i], l[j], p):
                    if p[0] == True:
                        d[j].append(i)
                    if p[1] == True:
                        d[i].append(j)
            elif abs(len(l[i]) - len(l[j])) == 1:
                y = codn2(l[i], l[j])
                if y == 1:
                    d[j].append(i)
                if y == 2:
                    d[i].append(j)
ans = 0
for i in range(n):
    ans = max(ans, longest(i))
print(ans + 1)
