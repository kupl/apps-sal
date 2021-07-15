def logical_calc(array, op):
  return eval({ 'AND': '&', 'OR': '|', 'XOR': '^' }[op].join(map(str, array)))
