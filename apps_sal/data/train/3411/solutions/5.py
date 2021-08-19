def amort(rate, bal, term, num):
    c = bal * rate / 1200 / (1 - (1 + rate / 1200) ** (-term))
    for i in range(num):
        int = bal * rate / 1200
        bal = bal + int - c
    return 'num_payment %d c %.0f princ %.0f int %.0f balance %.0f' % (num, c, c - int, int, bal)
