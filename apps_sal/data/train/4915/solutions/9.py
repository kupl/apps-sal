def rake_garden(g):
    return ' '.join((['gravel', 'rock'][e == 'rock'] for e in g.split()))
