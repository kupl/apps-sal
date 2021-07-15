def series_sum(n):
    array = []
    for i in range(n):
        array.append(1/(1 + 3 * i))
    return f'{sum(array):.2f}'
