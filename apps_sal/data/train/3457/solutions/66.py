def final_grade(e, p):
  s = 0
  if e > 90 or p > 10:
    s = 100
  elif e > 75 and p > 4:
    s = 90
  elif e > 50 and p > 1:
    s = 75
  return s

