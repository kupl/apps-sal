def nth_perm(n, d):
    st, i, n, fc = list(map(str, range(d))), 1, n - 1, ''
    while n:
        n, mod = divmod(n, i)
        fc = str(mod) + fc
        i += 1
    return ''.join([st.pop(int(i)) for i in fc.zfill(d)])
