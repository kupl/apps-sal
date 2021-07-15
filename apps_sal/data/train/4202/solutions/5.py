from collections import Counter

def ulam_sequence(u0, u1, n):

    seen, lst = {u0,u1}, [u0,u1]
    while len(lst) < n:
    
        c = Counter(v+w for i,v in enumerate(lst) for w in lst[i+1:] if v+w not in seen)
        cnd = min(filter(lambda kv: kv[1]==1, c.items()),
                  key=lambda kv: kv[0])[0]
                  
        lst.append(cnd)
        seen.add(cnd)
        
    return lst
