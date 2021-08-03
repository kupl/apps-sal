def calc_balance(r, n, bal, c):
    return (1 + r)**n * bal - (((1 + r)**n - 1) / r) * c


def amort(rate, bal, term, num_payment):
    r = rate / 100 / 12
    n = r * bal
    d = 1 - (1 + r)**(-term)
    c = n / d

    new_balance = calc_balance(r, num_payment, bal, c)
    old_balance = calc_balance(r, num_payment - 1, bal, c)
    princ = old_balance - new_balance
    intr = c - princ

    return "num_payment {} c {:.0f} princ {:.0f} int {:.0f} balance {:.0f}".format(num_payment, c, princ, intr, new_balance)
