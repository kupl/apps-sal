def build_square(sq):
    def A(x): return all(sq.count(i) >= x.count(i) for i in x)
    for _ in range(4):
        t = next(([sq.pop(sq.index(l)) for l in k] for k in [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]] if A(k)), 0)
        if not t:
            return False
    return True
