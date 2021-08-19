def final_grade(e, p):
    return [0, 75, 90, 100][sum([e > 90 or p > 10, e > 75 and p > 4 or (e > 90 or p > 10), e > 50 and p > 1 or (e > 90 or p > 10)])]
