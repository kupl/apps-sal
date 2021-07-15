def changer(string):
  return string.lower().translate(str.maketrans('abcdeffghijklmnopqrstuvwxyz', 'bcdEffghIjklmnOpqrstUvwxyzA'))
