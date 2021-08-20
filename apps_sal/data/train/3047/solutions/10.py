def repeating_fractions(n, d):
    a = str(n / d).split('.')
    (pos, out, m) = (0, '', False)
    while pos < len(a[1]) - 1:
        if a[1][pos] == a[1][pos + 1]:
            m = True
        else:
            out += m * '(' + a[1][pos] + m * ')'
            m = False
        pos += 1
    out += m * '(' + a[1][-1] + m * ')'
    return a[0] + '.' + out
