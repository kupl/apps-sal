def shoot(results):
  pete, phil = [sum(d[p].count('X') * (1+b) for d, b in results) for p in ['P1', 'P2']]
  return 'Pete Wins!' if pete > phil else 'Phil Wins!' if phil > pete else 'Draw!'
