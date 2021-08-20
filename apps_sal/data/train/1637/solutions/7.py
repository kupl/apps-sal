def shift(s):
    return sorted([s[-i:] + s[:-i] for i in range(len(s))])


def encode(s):
    if not s:
        return ('', 0)
    return (''.join([x[-1] for x in shift(s)]), shift(s).index(s))


def decode(s, n):
    if not s:
        return ''
    (first, last) = (sorted(s), list(s))
    res = ''
    i = n
    while len(res) < len(s):
        res += first[i]
        i = [k for k in range(len(s)) if last[k] == first[i]][[k for k in range(len(s)) if first[k] == first[i]].index(i)]
    return res
