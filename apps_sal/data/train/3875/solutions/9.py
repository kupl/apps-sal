FILLED = '■'
EMPTY = '□'
def draw(waves):
    result = ''
    height = max(waves)
    width = len(waves)
    matrix = [[EMPTY for x in range(width)] for y in range(height)]
    for y, value in enumerate(waves):
        for x in range(value):
            matrix[x][y] = FILLED
    for row in range(height-1, -1, -1):
        result = result + ''.join(matrix[row]) + '\n'
    return result.strip()
