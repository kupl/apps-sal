def lowercase_count(string):
  accum = 0
  abc = list('qwertyuioplkjhgfdsazxcvbnm')
  for i in string:
    if i in abc:
      accum += 1
  return accum
