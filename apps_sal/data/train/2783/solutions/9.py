def get_grade(*scores):
    grades = {
        10: 'A',
        9: 'A',
        8: 'B',
        7: 'C',
        6: 'D',
    }
    mean = sum(scores) / len(scores)
    return grades.get(mean // 10, 'F')

