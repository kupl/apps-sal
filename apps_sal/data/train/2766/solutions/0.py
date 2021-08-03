def check_concatenated_sum(n, r):
    return abs(n) == sum(int(e * r) for e in str(abs(n)) if r)
