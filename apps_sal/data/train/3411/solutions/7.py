def amort(r, p, n, x):
    r = r / 12 / 100
    c = (r * p) / (1 - ((1 + r)**(-n)))
    curr = p * (1 + r)**x - ((1 + r)**(x) - 1) * (c / r)
    i = r * (p * (1 + r)**(x - 1) - ((1 + r)**(x - 1) - 1) * (c / r))
    return f'num_payment {x} c {round(c)} princ {round(c-i)} int {round(i)} balance {round(curr)}'
