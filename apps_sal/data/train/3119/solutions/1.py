def pattern(n, y=1, *a):
    if n < 1: return ''
    l, y  = 2*n-1, max(1,y)
    sngl  = ['{}{}{}'.format(x%10, ' '*(l-2*x), x%10 if x!=n else '').center(l) for x in range(1,n+1)]
    cross = sngl + sngl[:-1][::-1]
    return '\n'.join( cross + cross[1:]*(y-1) )
