def expanded_form(n):
    return (lambda s: ' + '.join(s[x] + len(s[x + 1:]) * '0' for x in range(len(s))if s[x] != '0'))(str(n))
