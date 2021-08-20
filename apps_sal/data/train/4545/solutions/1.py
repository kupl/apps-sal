import cmath
_SECTORS = [6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11, 8, 16, 7, 19, 3, 17, 2, 15, 10]
_RESULTS = [(12.7, 'DB'), (31.8, 'SB'), (198.0, '{}'), (214.0, 'T{}'), (324.0, '{}'), (340.0, 'D{}')]
_SLICE = math.pi / 20.0


def get_score(x, y):
    point = complex(x, y)
    (distance, angle) = cmath.polar(point)
    i = 0 if abs(angle) < _SLICE else int(round(angle / _SLICE / 2))
    sector = _SECTORS[i]
    result = next((fmt for (diameter, fmt) in _RESULTS if distance < diameter / 2.0), 'X')
    return result.format(sector)
