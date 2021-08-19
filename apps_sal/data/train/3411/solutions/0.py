def amort(rate, bal, term, num_payments):
    monthlyRate = rate / (12 * 100)
    c = bal * (monthlyRate * (1 + monthlyRate) ** term) / ((1 + monthlyRate) ** term - 1)
    newBalance = bal
    for i in range(num_payments):
        interest = newBalance * monthlyRate
        princ = c - interest
        newBalance = newBalance - princ
    return 'num_payment %s c %.0f princ %.0f int %.0f balance %.0f' % (num_payments, c, princ, interest, newBalance)
