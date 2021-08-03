def grader(n):
    return "FDCBAF"[(n >= .6) + (n >= .7) + (n >= .8) + (n >= .9) + (n > 1)]
