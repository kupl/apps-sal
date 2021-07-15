def amort(rate, bal, term, num_payments):
    r = rate / (100 * 12)
    n = r * bal
    d = 1 - (1 + r) ** (-term)
    c = n / d
    for i in range(num_payments):
        int_ = r * bal
        princ = c - int_        
        bal -= princ
    return "num_payment %d c %.0f princ %.0f int %.0f balance %.0f" % (num_payments, c, princ, int_, bal)
