def get_grade(s1, s2, s3):
    result = sum([s1, s2, s3]) // 30
    if result >= 9:
        return 'A'
    elif result >= 8:
        return 'B'
    elif result >= 7:
        return 'C'
    elif result >= 6:
        return 'D'
    else:
        return 'F'

