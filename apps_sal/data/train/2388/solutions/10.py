def jiashen(new_tree):
    nonlocal g
    nonlocal k
    js = []
    for i in new_tree:
        for j in gra[i]:
            if (fil[j]):
                fil[j] = 0
                js.append(j)
                g += 1
                if (k):
                    d2.append(j)
                else:
                    d1.append(j)
    k = False if k else True
    return js

t = int(input())
zong = []
for _ in range(t):
    n, m = map(int, input().split())
    gra = [[] for i in range(n)]
    d1 = [0]
    d2 = []
    fil = [1 for i in range(n)]
    fil[0] = 0
    for i in range(m):
        a, b = map(int, input().split())
        gra[a-1].append(b-1)
        gra[b-1].append(a-1)
    new_tree = [0]
    k = True
    g = 1
    while (g < n):
        new_tree = jiashen(new_tree)
    le = len(d1)
    if (le <= n//2):
        zong.append(str(le)+'\n'+' '.join([str(x+1) for x in d1]))
    else:
        zong.append(str(n-le)+'\n'+' '.join([str(x+1) for x in d2]))
print('\n'.join(zong))
