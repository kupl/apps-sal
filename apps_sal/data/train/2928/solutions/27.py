def alphabet_war(fight):
  s = {'w':4,'p':3,'b':2,'s':1,'m':-4,'q':-3,'d':-2,'z':-1}
  x = sum(s[c] for c in fight if c in s)
  return 'Let\'s fight again!' if x == 0 else ['Left','Right'][x < 0]+' side wins!'
