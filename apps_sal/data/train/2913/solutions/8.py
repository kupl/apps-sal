def x(n):
    tmpl = '\n'.join(''.join('{1}' if j in (i, n - i - 1) else '{0}' for j in range(n)) for i in range(n))
    return tmpl.format('□', '■')

