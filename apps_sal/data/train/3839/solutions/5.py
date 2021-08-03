def score_test(tests, right, omit, wrong):
    return sum(right if a == 0 else omit if a == 1 else -wrong for a in tests)
