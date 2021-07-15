def score_test(tests, right, omit, wrong):
    awards = [right, omit, -wrong]
    return sum(map(awards.__getitem__, tests))
