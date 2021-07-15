def rake_garden(garden):
    return ' '.join(element  if element == 'gravel' or element == 'rock' else 'gravel' for element in garden.split())
