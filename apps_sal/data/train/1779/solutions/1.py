def balanced_parens(n):
    def push_in(s, n1, n2):
        if n1 + n2 == n * 2:
            res.append(s)
            return
        if n1 < n:
            push_in(s + '(', n1 + 1, n2)
        if n1 - n2 > 0:
            push_in(s + ')', n1, n2 + 1)

    res = []
    push_in('', 0, 0)

    return res
