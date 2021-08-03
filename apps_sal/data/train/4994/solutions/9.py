def word_problem(r, s1, s2, c):
    if s1 == s2:
        return True
    ix = {s1}
    for _ in range(c):
        xi = set()
        for s in ix:
            for x, y in r:
                if x in s:
                    i = s.find(x)
                    while i != -1:
                        ns = s[:i] + y + s[i + len(x):]
                        if ns == s2:
                            return True
                        xi.add(ns)
                        i = s.find(x, i + 1)
        ix = xi
    return False
