def well(x):
  good_ideas = x.count('good')
  if good_ideas == 0:
       return 'Fail!'
  elif good_ideas <= 2:
      return 'Publish!'
  else:
      return 'I smell a series!'
