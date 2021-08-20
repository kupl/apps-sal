KEEP = ['gravel', 'rock']
REPLACE_WITH = 'gravel'


def rake_garden(garden):
    return ' '.join([item if item in KEEP else REPLACE_WITH for item in garden.split()])
