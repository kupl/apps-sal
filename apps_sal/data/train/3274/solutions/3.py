def solve(st):
    i = len(st)//2
    while i and not st.endswith(st[0:i]): i -= 1
    return i;

