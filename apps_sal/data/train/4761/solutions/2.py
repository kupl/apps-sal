def search_k_from_end(ll, k):
    
    def _loop(n):
        if not n: return 1, None
        r = _loop(n.__next__)
        return 1 + r[0], r[1] if r[0] != k else n.data

    return _loop(ll.head)[1]

