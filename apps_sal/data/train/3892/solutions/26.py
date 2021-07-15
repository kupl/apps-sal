def grader(s):
    if s >= 0.9 and s<=1:
        return 'A'
    elif s>=0.8 and s<0.9:
        return 'B'
    elif s>= 0.7 and s<0.8:
        return 'C'
    elif s>= 0.6 and s<0.7:
        return 'D'
    else:
        return 'F'

