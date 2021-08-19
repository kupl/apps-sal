def shoot(results):
    (pete, phil) = (sum((r[player].count('X') * (1 + dbl) for (r, dbl) in results)) for player in ['P1', 'P2'])
    return 'Pete Wins!' if pete > phil else 'Phil Wins!' if phil > pete else 'Draw!'
