def grader(input):
  if input > 1 or input < .6:
    return 'F'
  if input >= .9:
    return 'A'
  elif input >= .8:
    return 'B'
  elif input >= .7:
    return 'C'
  elif input >= .6:
    return 'D'
