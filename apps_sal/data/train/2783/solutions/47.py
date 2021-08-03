def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    return {10: 'A', 9: 'A', 8: 'B', 7: 'C', 6: 'D'}.get(score // 10, 'F')
