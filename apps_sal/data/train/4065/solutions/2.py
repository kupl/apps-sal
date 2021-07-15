pandigital = [int(''.join(p)) for p in __import__('itertools').permutations('0123456789')][2*3*4*5*6*7*8*9:]
get_sequence = lambda offset, size: (lambda idx: pandigital[idx: idx + size])(__import__('bisect').bisect_left(pandigital, offset))
