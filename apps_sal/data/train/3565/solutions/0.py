def solve(st, k):
    for l in sorted(st)[:k]:
        st = st.replace(l, '', 1)
    return st
