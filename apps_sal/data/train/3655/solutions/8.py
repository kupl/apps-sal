def my_crib(n):
    roof = '\n'.join('{0}/{1}\\{0}'.format(' '*(n-i),' _'[n==i]*i*2) for i in range(n+1))
    x = lambda a: '\n|'+a*n*2+'|'
    return roof + x(' ')*(n-1) + x('_')
