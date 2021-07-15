def s(m, b, e, v):
    v[b] += 1
    if v[b] > 1:
        return v
    for i in range(len(m[b])):
        if m[b][i] != e:
            v = s(m,m[b][i],b,v)
    return v

def isTree(m):
    v = [0]*len(m)
    v = s(m, 0, -1, v)
    return v == [1]*len(v)
