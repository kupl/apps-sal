def seven(m):
  steps = 0
  while len(str(m)) > 2:
    m = int(str(m)[:-1]) - 2*int(str(m)[-1])
    steps += 1
    if m%7 == 0 and len(str(m)) <= 2:
      break
  return (m, steps)
