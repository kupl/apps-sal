def grader(score):
    score *= 10
    return 'DCBAA'[int(score - 6)] if 6 <= score <= 10 else 'F'
