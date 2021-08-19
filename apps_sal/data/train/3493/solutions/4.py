def change_count(ch):
    total = float(0.0)
    ch = ch.split()
    for x in ch:
        if 'dollar' in x:
            total += 1.0
        if 'quarter' in x:
            total += 0.25
        if 'dime' in x:
            total += 0.1
        if 'nickel' in x:
            total += 0.05
        if 'penny' in x:
            total += 0.01
    return '${:.2f}'.format(total)
