def check_exam(e, a):
    return max(0, sum((4 * (x == y) or -1 for (x, y) in zip(e, a) if y)))
