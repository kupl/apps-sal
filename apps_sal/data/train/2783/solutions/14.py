def get_grade(*grades):
    mean = sum(grades) / len(grades)
    for score, grade in [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')]:
        if mean >= score:
            return grade
