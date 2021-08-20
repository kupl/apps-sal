def array_madness(squares, cubes):
    return sum((num ** 2 for num in squares)) > sum((num ** 3 for num in cubes))
