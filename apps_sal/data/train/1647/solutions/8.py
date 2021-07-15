def next_bigger(n):
    m = [d for d in str(n)]
    for d in range(len(m)-1, 0, -1):
        if max(m[d:]) > m[d-1]:
            i = min((x for x in range(d, len(m)) if m[x] > m[d-1]), key = lambda k : m[k])
            m[d-1], m[i] = m[i], m[d-1]
            m[d:] = sorted(m[d:])
            break
    else:
        return -1
    return int("".join(m))
