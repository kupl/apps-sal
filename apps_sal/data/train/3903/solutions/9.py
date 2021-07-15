def validate(message):
  ml = message.split()
  if len(ml) != 8:
      return False
  if ml[0] != 'MDZHB':
      return False
  if len(ml[1]) != 2 or not ml[1].isdigit():
      return False
  if len(ml[2]) != 3 or not ml[2].isdigit():
      return False
  if not ml[3].isalpha() or not ml[3].isupper():
      return False
  for x in ml[4:]:
      if len(x) != 2 or not x.isdigit():
          return False
  return True
