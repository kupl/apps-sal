def per(n):
    def p(n):
        q, r = divmod(n, 10)
        if q == 0:
            return n
        return r * p(q)

    ans = []
    while n // 10 > 0:
        n = p(n)
        ans.append(n)
    return ans
