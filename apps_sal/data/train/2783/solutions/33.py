def get_grade(s1, s2, s3):
    grade = ['F'] * 60 + ['D'] * 10 + ['C'] * 10 + ['B'] * 10 + ['A'] * 11
    scores = (s1 + s2 + s3) // 3
    return grade[scores]
