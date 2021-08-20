def asterisc_it(n):
    (s, out) = ('', [])
    if type(n) is int:
        s = str(n)
    elif type(n) is list:
        s = ''.join([str(n[x]) for x in range(len(n))])
    else:
        s = str(n)
    return s if len(s) <= 1 else ''.join([s[x] + '*' if int(s[x]) % 2 == 0 and int(s[x + 1]) % 2 == 0 else s[x] for x in range(len(s) - 1)]) + s[-1]
