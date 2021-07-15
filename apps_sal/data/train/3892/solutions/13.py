def grader(score):
    grade = 'A'
    if score < 0.6 or score > 1:
      grade = 'F'
    elif score < 0.7:
      grade = 'D'
    elif score < 0.8:
      grade = 'C'
    elif score < 0.9:
      grade = 'B'
    return grade

