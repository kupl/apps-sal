def get_grade(s1, s2, s3):
    letter_grades = {(90, 100): 'A', (80, 89): 'B', (70, 79): 'C', (60, 69): 'D', (0, 59): 'F'}
    grade = (s1 + s2 + s3) / 3
    for score in list(letter_grades.keys()):
        if score[0] <= grade <= score[1]: return letter_grades[score]
        
    

