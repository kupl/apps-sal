def grader(score):
    print(score)

    return 'F' if score > 1 or score < 0.6 else 'AABCD'[int(10 - score * 10)]
