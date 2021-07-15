def find_the_ball(start, swaps):
  pos = start
  for tup in swaps:
    if pos == tup[0]: pos = tup[1]
    elif pos == tup[1]: pos = tup[0]
  return pos
      
      

