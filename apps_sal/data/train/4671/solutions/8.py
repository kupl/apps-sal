def isTree(m):
    status = [(e, 0) for e in m[0]]
    seen = set([0]) if status else set()
    while status:
        (t, f) = status.pop()
        seen.add(t)
        for e in m[t]:
            if e != f:
                if e in seen:
                    return False
                seen.add(e)
                status.append((e, t))
    return len(seen) == len(m)
