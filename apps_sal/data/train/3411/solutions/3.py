def amort(rate, bal, term, num_payments):
    # monthly interest rate
    r = rate / 1200
    # monthly payment
    c = bal * (r / (1 - (1 + r)**(-term)))
    # balance last month
    b = bal * (1 + r)**(num_payments - 1) - c * (((1 + r)**(num_payments - 1) - 1) / r)
    # interest
    i = r * b
    # amortization
    a = c - i
    # new_balance
    b -= a
    return 'num_payment {} c {:.0f} princ {:.0f} int {:.0f} balance {:.0f}'.format(num_payments, c, a, i, b)
