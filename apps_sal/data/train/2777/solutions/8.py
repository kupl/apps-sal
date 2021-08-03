def solve(st):
    st = st.replace('(', '').replace(')', '')
    i = len(st)
    while i:
        i -= 1
        if st[i].isdigit():
            dg = int(st[i])
            ex = st[i + 1:] * dg
            st = st[:i] + ex
            i += dg
    return st
