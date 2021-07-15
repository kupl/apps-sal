def solve(st,k):
    if k >= len(st):
        return ""
    chars = sorted(st)
    for ch in chars[:k]:
        st = st.replace(ch, '', 1)
    return st
