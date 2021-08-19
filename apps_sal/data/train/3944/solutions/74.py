def sum_triangular_numbers(n):
    val = 0
    return_list = []
    if n < 0:
        return 0
    for x in range(1, n + 1):
        val = val + x
        return_list.append(val)
    return sum(return_list)
