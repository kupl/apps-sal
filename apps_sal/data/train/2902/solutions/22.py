def opposite(number):
  import re
  m = re.match("-", str(number))
  if m:
     number = re.sub("-", "", str(number))
  else:
     number = "-" + str(number)
  try:
    return int(number)
  except ValueError:
    return float(number)
