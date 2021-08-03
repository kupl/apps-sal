def find_difference(a, b):
    result_a = 1
    result_b = 1

    for i in a:
        result_a = result_a * i
    for t in b:
        result_b = result_b * t

    return abs(result_b - result_a)
