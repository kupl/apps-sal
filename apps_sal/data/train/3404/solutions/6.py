def solve(st,a,b):
    str = st[a:b+1]
    st = st.replace(st[a:b+1], str[::-1])
    return st
