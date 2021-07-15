def moment_of_time_in_space(moment):
  l = [int(i) for i in moment if i.isdigit() and i != '0']
  time = sum(l)
  space = 8 - len(l)
  return [True, False, False] if space > time else\
 ([False, True, False] if space==time else [ False,  False, True])
