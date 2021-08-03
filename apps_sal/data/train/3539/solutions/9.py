def norm_index_test(seq, n):
    try:
        return seq[n % len(seq)]
    except ZeroDivisionError:
        return None
