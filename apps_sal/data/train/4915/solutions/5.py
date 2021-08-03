def rake_garden(g): return ' '.join('gravel' if e not in ['gravel', 'rock'] else e for e in g.split())
