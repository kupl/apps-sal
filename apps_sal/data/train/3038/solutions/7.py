def solve(st):
    d = dict(((st.rfind(c) - st.find(c), c) for c in sorted(st)[::-1]))
    return d[max(d)]
