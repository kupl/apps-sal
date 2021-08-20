def score_test(tests, right, omit, wrong):
    right_score = tests.count(0) * right
    omit_score = tests.count(1) * omit
    wrong_score = tests.count(2) * wrong
    return right_score + omit_score - wrong_score
