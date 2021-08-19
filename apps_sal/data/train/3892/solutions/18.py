def grader(s):
    return 'FDCBAA'[(int(s * 10) - 5) * (s >= 0.6 and s <= 1)]
