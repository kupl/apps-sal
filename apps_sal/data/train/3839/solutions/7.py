# returns test score
def score_test(tests: list, right: int, omit: int, wrong: int) -> int:
    right_count = tests.count(0)
    omit_count = tests.count(1)
    wrong_count = tests.count(2)
    return right_count * right + omit_count * omit - wrong_count * wrong
