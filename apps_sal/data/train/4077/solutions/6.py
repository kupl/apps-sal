def premier_league_standings(teams):
  ret = {1:teams[1]}
  for i,name in enumerate(sorted(teams[i] for i in teams.keys() if i != 1)):
    ret[i+2] = name
  return ret
