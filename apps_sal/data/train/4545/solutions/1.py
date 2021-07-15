import cmath

# Dartboard sectors, beginning at 0 angle (i.e. middle of 6), continuing CCW:
_SECTORS = [6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11, 8, 16, 7, 19, 3, 17, 2, 15, 10]

# Diameters in increasing order, and resulting format string for score:
_RESULTS = [(12.7, 'DB'), (31.8, 'SB'), (198., '{}'), (214., 'T{}'), (324., '{}'), (340., 'D{}')] 

# 1/2 the angle of a single number on the board (since sectors don't start on 0 angle)
_SLICE = math.pi / 20.

def get_score(x,y):
    point = complex(x, y)
    distance, angle = cmath.polar(point)
    
    # Negative angles work by indexing the sector list with a negative index!
    # The check against "< _SLICE" takes care of the wraparound at '6':
    i = 0 if abs(angle) < _SLICE else int(round(angle / _SLICE / 2))
    
    sector = _SECTORS[i]
    
    # Take the first format we reach in distance, and default to 'X' if we go beyond the board:
    result = next((fmt for diameter, fmt in _RESULTS if distance < diameter / 2.), 'X')
    return result.format(sector)
