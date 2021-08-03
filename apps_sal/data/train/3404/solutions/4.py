def solve(st, a, b):
    sub = st[a:b + 1]
    rev = sub[::-1]
    return st.replace(sub, rev)
