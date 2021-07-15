def strong_num(number):
  w = [int(i) for i in str(number)]
  res = []
  for i in w:
    f = 1
    for q in range(1,i + 1):
      f *= q
    res.append(f)
  z = sum(res)
  t = "".join(str(z))
  if str(number) == t:
    return 'STRONG!!!!'
  else:
    return 'Not Strong !!'
