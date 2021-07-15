from re import compile
build = compile(r"P(\d+)").findall
read = compile(r"p(\d+)(.*?)q").sub

def magic_call_depth_number(pattern):
    P = {}
    def filling(w):
        k, v = w.groups()
        P[k] = set(build(v))
        return ""
    
    def minimum(id1, S):
        if id1 in S: return (False, -1)
        if not P[id1]: return (True, 0)
        mini = float('inf')
        for id2 in P[id1]:
            b, x = minimum(id2, S|{id1})
            if b: return (True, 0)
            mini = min(mini, x+1)
        return (False, mini)
    
    def maximum(id1, S):
        if id1 in S: return (True, -1)
        if not P[id1]: return (False, 0)
        res, maxi = (False, 0)
        for id2 in P[id1]:
            b, x = maximum(id2, S|{id1})
            if b: res, maxi = res or b, max(maxi, x+1)
        return (res, maxi)
    
    P[None] = set(build(read(filling, pattern)))
    return [minimum(None, set())[1], maximum(None, set())[1]]
