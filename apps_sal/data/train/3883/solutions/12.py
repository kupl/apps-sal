def solve(s):
    (c, v, r) = ([], [], [])
    for m in s:
        if m in 'aeiou':
            v.append(m)
        else:
            c.append(m)
    c.sort()
    v.sort()
    (cl, vl) = (len(c), len(v))
    if abs(cl - vl) > 1:
        return 'failed'
    for i in range(max(cl, vl)):
        if vl >= cl:
            if i < vl:
                r.append(v[i])
            if i < cl:
                r.append(c[i])
        else:
            if i < cl:
                r.append(c[i])
            if i < vl:
                r.append(v[i])
    return ''.join(r)
