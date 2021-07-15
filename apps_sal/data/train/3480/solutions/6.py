from decimal import Decimal

def sequence_sum(s, e, step):
    if s > e and step > 0 or s < e and step < 0: return 0
    elems = abs(s - e) // abs(step) + 1
    last = s + (step * (elems - 1))
    avg = (s + last) / 2
    return int(Decimal(elems)* Decimal(avg))
