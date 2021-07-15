def ride(group,comet):
  command = {True:'GO', False:'STAY'}
  num = lambda st: reduce(lambda x,y: x*y, map(lambda x: ord(x)-ord('A')+1, st))%47
  return command[num(group)==num(comet)]
