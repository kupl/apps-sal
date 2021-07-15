def grader(score):
    if score<0.6 or score>1:
        return 'F'
    if score>=0.6 and score<0.7:
        return 'D'
    if score>=0.7 and score<0.8:
        return 'C'
    if score>=0.8 and score<0.9:
        return 'B'
    if score>=0.9:
        return 'A'

