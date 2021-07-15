def final_grade(exam, projects):
    if 90 < exam or 10 < projects:
      return 100
    if 75 < exam and 5 <= projects:
      return 90
    if 50 < exam and 2 <= projects:
      return 75
    return 0
