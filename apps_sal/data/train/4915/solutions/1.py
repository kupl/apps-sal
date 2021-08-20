def rake_garden(garden):
    return ' '.join((w if w == 'rock' else 'gravel' for w in garden.split()))
