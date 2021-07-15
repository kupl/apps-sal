def grader(n):
    return 'F' if n > 1 or n < .6 else 'A' if n >= .9 else 'B' if n >= .8 else 'C' if n >= .7 else 'D'
