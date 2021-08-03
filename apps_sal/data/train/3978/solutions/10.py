def check_for_factor(base, factor):
    f = [i for i in range(1, base + 1) if base / i == base // i]
    return True if factor in f else False
    # your code here
