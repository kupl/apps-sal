def amort(rate, bal, term, num_payments):
    r=rate/(1200)
    c=r*bal/(1-(1+r)**(-term))
    for _ in range(num_payments):
        _int=bal*r
        princ=c-_int
        bal-=princ
    return 'num_payment {} c {:.0f} princ {:.0f} int {:.0f} balance {:.0f}'.format(num_payments,c,princ,_int,bal)
