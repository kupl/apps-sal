def balanced_num(n):
    sn = str(n)
    mn = len(sn) // 2
    fn = sum(map(int, sn[:mn - 1]))
    scn = sum(map(int, sn[mn + 1:]))
    if len(sn) % 2:
        (scn, fn) = (sum(map(int, sn[mn + 1:])), sum(map(int, sn[:mn])))
    print(n, fn, scn)
    return 'Balanced' if n < 100 or fn == scn else 'Not Balanced'
