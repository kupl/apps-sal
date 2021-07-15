def min_value(digits):
    return int(''.join(str(e)for e in sorted(dict.fromkeys(digits))) )
