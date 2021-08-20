def check_exam(a1, a2):
    return max(0, sum((4 if i == j else -1 for (i, j) in zip(a1, a2) if j)))
