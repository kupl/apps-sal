def elections_winners(a,k):
    m = max(a)
    v = [i+k for i in a if i+k>m]
    if k == 0 and not v and a.count(m)==1: return 1
    return len(v)
