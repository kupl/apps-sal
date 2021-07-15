#returns test score
def score_test(tests, right, omit, wrong):
    result = 0
    for score in tests:
        if score == 0:
            result += right
        elif score == 1:
            result += omit
        elif score == 2:
            result -= wrong
    return result

