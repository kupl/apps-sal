def table_game(t):
  l = [t[0][0],t[0][2],t[2][0],t[2][2]]
  return l if sum(l) == t[1][1] and sum(sum(t,[])) == sum(l) * 4 else [-1]
