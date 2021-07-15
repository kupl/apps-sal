import re

def find_missing_number(sequence):
  if len(sequence) == 0:
      return 0
  elif not sequence.replace(" ", "").isnumeric():
      return 1
  list1 = [int(i) for i in sequence.split(" ")]
  maxNum = max(list1)
  if maxNum >= 10:
    for i in range(1, maxNum):
      s = str(i)
      if re.search('(:?(:?[^0-9]|^)'+s+' | '+s+'(:?[^0-9]|$))', sequence) == None:
        return i
  else:
    for i in range(1, maxNum):
      if str(i) not in sequence:
        return i
  return 0
