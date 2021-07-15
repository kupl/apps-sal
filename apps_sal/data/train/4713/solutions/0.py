from itertools import permutations

def late_clock(digits):
  for p in permutations(sorted(digits, reverse=True)):
    if p[0] > 2 or (p[0] == 2 and p[1] > 3) or p[2] > 5: continue
    return '{}{}:{}{}'.format(*p)
