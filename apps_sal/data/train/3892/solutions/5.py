def grader(score):
  return 'F' if score > 1 or score < 0.6 else 'ABCD'[int(10 * (0.999 - score))]
