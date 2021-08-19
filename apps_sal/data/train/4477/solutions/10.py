def reverse_number(n):
    n_rev = int(''.join(reversed([c for c in str(n) if c.isdigit()])))
    return n_rev if n >= 0 else -n_rev
