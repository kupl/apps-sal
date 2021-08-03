def largest_rect(h):
    r, s, i, l = 0, [], 0, len(h)
    while i < l:
        if not s or h[s[-1]] <= h[i]:
            s.append(i)
            i += 1
        else:
            t = s.pop()
            a = i - s[-1] - 1 if s else i
            a *= h[t]
            r = r if r > a else a
    while s:
        t = s.pop()
        a = i - s[-1] - 1 if s else i
        a *= h[t]
        r = r if r > a else a
    return r
