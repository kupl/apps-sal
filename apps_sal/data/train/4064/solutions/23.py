def count_by(x, n):
    array = []

    for i in range(x, n * x + 1, x):
        array.append(i)

    return array
