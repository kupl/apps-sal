def grader(score):
    return 'F' if score > 1 or score < 0.6 else 'FAFFFFDCBA'[int(str(score*10)[0])]

