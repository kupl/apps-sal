def alphabet_war(fight):

  s = 'wpbsszdqm'
  alive = []

  if '*' not in fight[:2]:
    alive.append(fight[0])

  for i, c  in enumerate(fight[1:], 1):
    if '*' not in fight[i-1:i+2]:
      alive.append(c)
  
  x = sum(4 - s.index(c) for c in alive if c in s)
  return 'Let\'s fight again!' if x==0 else ['Left','Right'][x<0] + ' side wins!'
