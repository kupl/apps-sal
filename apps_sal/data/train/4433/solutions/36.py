from functools import reduce
logical_calc = lambda l,op:reduce(lambda a,b:a and b if op == 'AND' else a or b if op == 'OR' else a != b,l)
