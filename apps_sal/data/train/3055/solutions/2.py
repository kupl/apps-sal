def sum_str(*values):
    return str(sum((int(s or '0') for s in values)))
