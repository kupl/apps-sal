def reverse_number(n):
    r = str(n).replace('-', '')[::-1]
    return int(r) if n > 0 else -int(r)
