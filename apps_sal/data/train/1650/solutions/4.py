def ways(t, n, d):
    return [e for l in [[int(str(i)+str(e)) for e in ways(t-i, n-1, [k for k in d if k>= i])] for i in d] for e in l] if n > 1 else [t] if t in d else []

def find_all(target, n):
    r = ways(target, n, [1,2,3,4,5,6,7,8,9])
    return [len(r), min(r), max(r)] if r else []
