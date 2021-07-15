def pascal(p):
    triangle = [[1]]
    for _ in range(p - 1):
        to_sum = list(zip([0] + triangle[-1], triangle[-1] + [0]))
        triangle.append(list(map(sum, to_sum)))
    return triangle

