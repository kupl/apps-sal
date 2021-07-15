def get_grade(s1, s2, s3):
  m = (s1 + s2 + s3) / 3
  return 'A' if m >= 90 else 'B' if m >= 80 else 'C' if m >= 70 else 'D' if m >= 60 else 'F'
