def solve(a,b):
    print((a,b))
    if sorted(a)==sorted(b) or (set(list(a))==set(list(b))):
        return 0
    for x in b:
        for x in a:
            if a.count(x)<b.count(x)  : return 0
    else: return len(a)-len(b)    
