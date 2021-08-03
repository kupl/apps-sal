def create_postions():
    p1 = [0, 1, 2] * 9
    p2 = [*[0] * 3, *[1] * 3, *[2] * 3] * 3
    p3 = [0] * 9 + [1] * 9 + [2] * 9
    arr = list(zip(p1, p2, p3))

    return lambda n: arr[n % 27]


get_positions = create_postions()
