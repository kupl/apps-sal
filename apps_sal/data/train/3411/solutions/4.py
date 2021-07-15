def amort(rate, bal, term, num_payments):
    # your code
    r = rate / (100 * 12)
    c = (r * bal) / (1 - pow((1 + r), -term))
    
    int = 0
    princ = 0
    for n in range(num_payments):
        int = r * bal
        princ = c - int
        bal -= princ
    
    return "num_payment {:0.0f} c {:0.0f} princ {:0.0f} int {:0.0f} balance {:0.0f}".format(num_payments, c, princ, int, bal)
