def reverse_by_center(s):
    (q, r) = divmod(len(s), 2)
    return s[-q:] + s[q:q + r] + s[:q]
