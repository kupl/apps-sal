def apple(x):
  number = 0
  if not (type(x) is int):
    number = int(x)
  else:
    number = x
  
  if number >= 32:
    return "It's hotter than the sun!!"
  else:
    return "Help yourself to a honeycomb Yorkie for the glovebox."

