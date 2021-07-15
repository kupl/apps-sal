def alphabet_war(fight):
  left = {'w':4,'p':3,'b':2,'s':1}
  rigth = {'m':4,'q':3,'d':2,'z':1}
  leftp = 0
  rigthp = 0
  for e in fight:
    leftp += left.get(e,0)
    rigthp += rigth.get(e,0)
  if leftp > rigthp:
    return'Left side wins!'
  elif rigthp > leftp:
    return 'Right side wins!'
  else:
    return "Let's fight again!"
