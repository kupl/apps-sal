import re

def solve(s):
    elements = re.split('[azertyuiopqsdfghjklmwxcvbn]',s)
    return max([int(coordinates) for coordinates in elements if len(coordinates) > 0 ])
