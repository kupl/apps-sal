def solve(st, a, b):
    str = st[a:b + 1]
    str_new = str[::-1]
    res = st.replace(str, str_new)
    return res
