def balanced_num(n):
    s = [int(i) for i in list(str(n))]
    l = s[:len(s) // 2]
    r = s[-1:len(s) // 2:-1]
    if len(s) == len(l) * 2:
        l = l[:-1]
        s = s[:-1]
    if sum(l) == sum(r):
        return 'Balanced'
    else:
        return 'Not Balanced'
