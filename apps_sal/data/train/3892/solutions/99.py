def grader(score):
    rez = int(score * 100)
    if rez > 100 or rez < 60:
        return 'F'
    elif 90 <= rez <= 100:
        return 'A'
    elif 80 <= rez < 90:
        return 'B'
    elif 70 <= rez < 80:
        return 'C'
    elif 60 <= rez < 70:
        return 'D'
