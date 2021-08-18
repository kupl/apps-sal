def modpow(a, x):
    if(x == 0):
        return 1
    elif(x % 2 == 0):
        t = modpow(a, x / 2)
        return (t * t) % (1000000007)
    else:
        t = modpow(a, x / 2)
        return (t * t * a) % (1000000007)


T = eval(input())
ans = [0] * T
for j in range(T):
    [N, Q] = [int(x) for x in (input()).split()]
    for i in range(N - 1):
        input()
    comp = list(range(N + 1))
    revcomp = []
    for i in range(N + 1):
        revcomp.append([i])
    sumcomp = [0] * (N + 1)
    flag = True
    rank = 0
    for i in range(Q):
        if(not(flag)):
            input()
        else:
            [u, v, x] = [int(x) for x in (input()).split()]
            if(comp[u] == comp[v]):
                if(not((sumcomp[u] + sumcomp[v]) % 2 == (x % 2))):
                    flag = False
            else:
                rank = rank + 1
                n1 = len(revcomp[comp[u]])
                n2 = len(revcomp[comp[v]])
                if(n1 < n2):
                    oldsu = sumcomp[u]
                    l = revcomp[comp[v]]
                    for w in revcomp[comp[u]]:
                        l.append(w)
                        comp[w] = comp[v]
                        sumcomp[w] = (sumcomp[w] + sumcomp[v] + x + oldsu) % 2
                else:
                    oldsv = sumcomp[v]
                    l = revcomp[comp[u]]
                    for w in revcomp[comp[v]]:
                        l.append(w)
                        comp[w] = comp[u]
                        sumcomp[w] = (sumcomp[w] + sumcomp[u] + x + oldsv) % 2
    if(not(flag)):
        ans[j] = 0
    else:
        ans[j] = modpow(2, (N - rank - 1))

for j in range(T):
    print((ans[j]))
