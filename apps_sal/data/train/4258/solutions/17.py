def series_sum(number):
    solution = sum((1 / (1 + 3 * i) for i in range(number)))
    return format(solution, '.2f')
