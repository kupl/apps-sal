def final_grade(exam, projects):
  finalGrade = 0;
  if exam > 50 and projects >= 2:
    finalGrade = 75;
  if exam > 75 and projects >= 5:
    finalGrade = 90;
  if exam > 90 or projects > 10:
    finalGrade = 100;
  return finalGrade;
