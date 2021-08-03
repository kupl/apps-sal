def mean(nums): return sum(nums) / (len(nums) + .0)


def get_grade(s1, s2, s3):
    m = mean([s1, s2, s3])
    if m >= 90:
        return 'A'
    elif m >= 80:
        return 'B'
    elif m >= 70:
        return 'C'
    elif m >= 60:
        return 'D'
    else:
        return "F"
