def grader(score):
    return (score < 0.6 or score > 1) and 'F' or (score < 0.7 and 'D') or (score < 0.8 and 'C') or (score < 0.9 and 'B') or 'A'
