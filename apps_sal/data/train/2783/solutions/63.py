def get_grade(s1, s2, s3):
    dic = {10: 'A', 9: 'A', 8: 'B', 7: 'C', 6: 'D', 5: 'F', 4: 'F', 3: 'F', 2: 'F', 1: 'F', 0: 'F'}
    return dic[(s1 + s2 + s3) / 3 // 10]
