def splitlist(l, i=0, sa=0, sb=0, sl=None, mem=None, first=False):
    if mem is None: first, mem, sl = True, {}, sum(l); 
    if i == len(l): return ([], []) if first else (abs(sa-sb), [])
    found = mem.get((i,sa)); da = db = sl
    if not found and sa < sl/2: da, ma = splitlist(l, i+1, sa+l[i], sb, sl, mem); ma=[True]+ma
    if not found and da > 0 and sb < sl/2: db, mb = splitlist(l, i+1, sa, sb+l[i], sl, mem); mb=[False]+mb
    if not found: found = mem.setdefault((i, sa), (da, ma) if da<=db else (db, mb))
    if not first: return found
    a, b = [], []
    for v, m in zip(l, found[1]): (a if m else b).append(v)
    return a, b
