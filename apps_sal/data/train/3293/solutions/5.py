ONES = set(((0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0)))


def rule30(array, n):
    if n < 1:
        return array
    array = (0,) + tuple(1 if v == 1 else 0 for v in array) + (0,)
    for _ in range(n):
        array = (array[-1], 0) + array + (0, array[0])
        array = tuple(int(array[i: i + 3] in ONES) for i in range(len(array) - 2))
    return list(array[1:-1])
