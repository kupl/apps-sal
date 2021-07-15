def mem_alloc(t):
    visited, l = set(), len(t)
    while 1:
        m = max(t)
        ind = t.index(m)
        t[ind], put = 0, m//l
        for i in range(l) : t[i] += put
        for i in range(ind+1,ind+(m-put*l)+1) : t[i % l] += 1
        m = tuple(t)
        if m in visited : return len(visited)+1
        visited.add(m)
