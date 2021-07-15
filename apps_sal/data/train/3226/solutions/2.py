def land_perimeter(arr):
    result = 0
    for row in arr + list(zip(*arr)):
        current = list(row)
        result += sum(a != b for a, b in zip(['O'] + current, current + ['O']))
    return 'Total land perimeter: {}'.format(result)

