def amort(rate, bal, term, num_payments):
    r = rate / 1200
    c = bal * (r / (1 - (1 + r)**(-term)))
    b = bal * (1 + r)**(num_payments - 1) - c * (((1 + r)**(num_payments - 1) - 1) / r)
    i = r * b
    a = c - i
    b -= a
    return 'num_payment {} c {:.0f} princ {:.0f} int {:.0f} balance {:.0f}'.format(num_payments, c, a, i, b)
