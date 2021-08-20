def div(n):
    return [[i, n // i] for i in range(2, int(n ** 0.5) + 1) if not n % i]


def prod_int_partII(n, s):
    (li, parts) = (div(n), set())

    def recur(li, s=[]):
        parts.add(tuple(sorted(s)))
        for i in li:
            recur(div(i[1]), s + i if not s else s[:-1] + i)
    recur(li)
    req = sorted(filter(lambda x: len(x) == s, parts))
    return [len(parts) - 1, len(req), list([map(list, req), req[0]][len(req) == 1]) if req else []]
