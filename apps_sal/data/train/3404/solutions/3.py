def solve(st, a, b):
    sub, rev = st[a:b + 1], st[a:b + 1][::-1]
    return st.replace(sub, rev)
