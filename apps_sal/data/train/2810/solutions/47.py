def solve(x):
    return [len([e for i,e in enumerate(i) if ord(e.lower())-97==i])for i in x]
