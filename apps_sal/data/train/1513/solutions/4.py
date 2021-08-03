# cook your dish here
try:
    X = list(map(int, input().split()))
except:
    X = [0, 0]
ch = []
chnew = []
par = {}
par[1] = 0
for i in range(X[0] + 1):
    ch.append([])
    chnew.append([])
for i in range(X[0] - 1):
    Y = list(map(int, input().split()))
    # par[Y[1]]=[Y[0],Y[2]]
    ch[Y[0]].append([Y[1], Y[2]])
    ch[Y[1]].append([Y[0], Y[2]])
tre = [1]
while(len(tre)):
    cr = tre[-1]
    tre = tre[:-1]
    for i in ch[cr]:
        chnew[cr].append(i)
        par[i[0]] = [cr, i[1]]
        tre.append(i[0])
        for j in ch[i[0]]:
            if(j[0] == cr):
                ch[i[0]].remove(j)
                break
ch = chnew


def goup(par, nd):
    if(nd == 1):
        return 0
    else:
        p = par[nd]
        ans = p[1] + goup(par, p[0])
        return (max([ans, 0]))


def godown(ch, nd):
    ans = 0
    for i in ch[nd]:
        ans = max([(i[1] + godown(ch, i[0])), ans])
    return(ans)


for i in range(X[1]):
    Z = list(map(int, input().split()))
    r = Z[0]
    s = Z[1]
    nans = 0
    while(r != s):
        if(r > s):
            nans = nans + par[r][1]
            r = par[r][0]
        else:
            nans = nans + par[s][1]
            s = par[s][0]
    if((r == Z[0]) or (r == Z[1])):
        if(Z[0] < Z[1]):
            nans = nans + 2 * max(goup(par, Z[0]), godown(ch, Z[1]))
        else:
            nans = nans + 2 * max(goup(par, Z[1]), godown(ch, Z[0]))
    else:
        nans = nans + 2 * goup(par, r)
    print(nans)
