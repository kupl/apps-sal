def wheat_from_chaff(values):
  negative = []
  positive = []
  while len(values) > 0:
    if values[0] < 0:
      negative.append(values.pop(0))
    elif values[-1] > 0:
      positive.append(values.pop(-1))
    else:
      positive.append(values.pop(0))
      negative.append(values.pop(-1))
  return negative+positive[::-1]

