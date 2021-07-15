from itertools import product
get_pins = lambda o: map(lambda x: ''.join(x), product(*
 ['08 124 1235 236 1457 24568 3569 478 05789 689'.split(' ')
 [int(e)] for e in o]))
