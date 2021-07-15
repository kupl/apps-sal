def solve(arr):
    r=[]
    for w in arr:
        r.append(sum(1 for i,c in enumerate(w.lower()) if ord(c)==ord('a')+i))
    return r
