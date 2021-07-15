def grader(score):
  if score > 1:
    return "F"
  for s, g in [(.9, "A"), (.8, "B"), (.7, "C"), (.6, "D")]:
    if score >= s:
      return g
  return "F"

