def hex_to_dec(s):
    su = 0
    l = ['a', 'b', 'c', 'd', 'e', 'f']
    n = len(s)
    n1 = n - 1
    for i in range(0, n):
        if '0' <= s[i] <= '9':
            su = su + int(s[i]) * (16**(n1))
            n1 = n1 - 1
        else:
            su = su + (10 + l.index(s[i].lower())) * (16**(n1))
            n1 = n1 - 1
    return su
