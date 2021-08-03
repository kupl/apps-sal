def reverse_by_center(s):
    n = len(s)
    m = n >> 1
    if n % 2:
        return s[m + 1:] + s[m] + s[:m]
    return s[m:] + s[:m]
