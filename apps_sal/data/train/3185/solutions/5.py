def rotate_against_clockwise(matrix, times):
    return list(map(list, zip(*matrix)))[::-1] if times % 4 == 1 else rotate_against_clockwise(list(map(list, zip(*matrix)))[::-1], times - 1)
