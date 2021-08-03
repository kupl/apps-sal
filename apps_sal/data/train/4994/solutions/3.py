def word_problem(rules, f, t, a):
    if f == t:
        return True
    if a == 0:
        return f == t
    return any(word_problem(rules, x, t, a - 1)for r in rules for x in apply(r, f))


def apply(r, f):
    x, y = r
    l = len(x)
    for i in range(len(f) - l + 1):
        if f[i:i + l] == x:
            yield f[:i] + y + f[i + l:]
