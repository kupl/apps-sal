def score_test(tests, right, omit, wrong):
    final = 0
    for scores in tests:
        if scores == 0:
            final = final + right
        elif scores == 1:
            final = final + omit
        elif scores == 2:
            final = final - wrong
    return final
