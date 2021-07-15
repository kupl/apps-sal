import re

COORD_RE = re.compile(r'(-?[\d]+\.?[\d]*), ?(-?[\d]+\.?[\d]*)$')
    
def is_valid_coordinates(coordinates):
    match = COORD_RE.match(coordinates)
    if not match: return False
    x, y = match.group(1), match.group(2)
    
    x, y = float(x), float(y)
    if not 0 <= abs(x) <= 90: return False
    if not 0 <= abs(y) <= 180: return False
    
    return True
