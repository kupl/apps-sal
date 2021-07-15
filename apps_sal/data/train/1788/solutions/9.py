from functools import reduce
def choose_move(game_state):

  cond = reduce(lambda x,y: x^y, game_state)
  
  for idx, val in enumerate(game_state):
    if (val^cond < val):
      return (idx, val - (val^cond))
  

