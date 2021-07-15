def pillow(s):
  fridges = set(i for i, v in enumerate(s[0]) if v == 'n')
  pillows = set(i for i, v in enumerate(s[1]) if v == 'B')
  return len(fridges & pillows) > 0
