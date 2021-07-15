def meeting(s):
  s = s.upper()
  s = s.split(';')
  array = []
  string = ""
  for i in s:
    i = i.split(':')
    string = '('+i[1]+', '+i[0]+')'
    array.append(string)
  array.sort()
  output = ""
  for j in array:
    output += j
  return output
