def solve(s):
    while '(' in s:
        l, r = s.rsplit('(', 1)
        ss, r = r.split(')', 1)
        s = (l[:-1] + ss * int(l[-1]) + r) if l[-1].isdigit() else l + ss + r
    return s
