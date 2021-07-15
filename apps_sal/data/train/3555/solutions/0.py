def hanoiArray(n):
    A, B, C = list(range(n, 0, -1)), [], []
    res = [str([A, C, B])]
    def rec(n, X, Y, Z):
        if not n: return
        rec(n-1, X, Z, Y)
        Y.append(X.pop())
        res.append(str([A, C, B]))
        rec(n-1, Z, Y, X)        
    rec(n, A, B, C)
    return '\n'.join(res)
