from itertools import count

def next_higher(start,k):

    def parts(n, s, p, store):
        if sum(store) > n:
            return
    
        if not s:
            if len(p) > 1:
                store.append(sum(p))
            return
    
        for i in range(1, len(s) + 1):
            parts(n, s[i:], p + [int(s[:i])], store)
    
        return store
    
    
    for m in count(start + 1):
        x = parts(m, str(m * k), [], [])

        if sum(x) == m:
            return m
