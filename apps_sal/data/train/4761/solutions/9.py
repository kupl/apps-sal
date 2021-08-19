def search_k_from_end(l, k):
    (m, n) = (l.head, l.head)
    while k:
        if not n:
            return None
        n = n.__next__
        k -= 1
    while n:
        m = m.__next__
        n = n.__next__
    return m and m.data
