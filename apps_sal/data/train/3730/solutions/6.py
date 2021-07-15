def capitalize(s):
  index = 0
  string1 = ""
  string2 = ""
  for i in s:
    if index % 2 == 0:
      string1 += i.upper()
      string2 += i
      index += 1
    else:
      string1 += i
      string2 += i.upper()
      index += 1
  return [string1, string2]
