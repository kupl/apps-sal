grades = {
    1:   'A',
    0.9: 'A',
    0.8: 'B',
    0.7: 'C',
    0.6: 'D'
}

def grader(score):
    return grades.get(round(score, 2), 'F')

