def reverse(st):
    st = st.split()
    print(st)
    out = []
    for i in range(len(st) - 1, -1, -1):
        out.append(st[i])
    out = ' '.join(out)
    return out
    return st
