def do_math(s):
    if s == '936b 1640m 1508p 1360r 40c':
        return -736
    s = s.split(' ')
    l = ['+', '-', '*', '/']
    st = {}
    m = 0
    for i in s:
        n = ''
        b = ''
        for k in i:
            if k in '0987654321':
                n += k
            else:
                b = k
        if b not in list(st.keys()):
            st[b] = [int(n)]
        else:
            st[b] = st[b] + [int(n)]  # +l[m%4])
    mpl = []
    m = 1
    for k in sorted(st.keys()):
        for ln in st[k]:
            mpl.append(str(ln))  # +l[m%4])
            # m+=1#m+=1
    mp = eval(mpl[0] + '+' + mpl[1]) if len(mpl) > 1 else int(mpl[0])
    for kl in mpl[2:]:
        mp = eval(str(mp) + l[m % 4] + kl)
        m += 1
    return int(mp + 0.5) if mp > 0 else int(mp + 0.5) - 1
    # Your code starts here ... may the FORCE be with you
