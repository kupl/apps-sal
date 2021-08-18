def my_crib(n):
    crib_string = ' ' * (2 * n) + '_' * (2 * n + 1) + ' ' * (2 * n) + '\n'
    for i in range(1, 2 * n + 1):
        crib_string += ' ' * (2 * n - i) + '/' + '_' * (2 * n + 2 * i - 1) + '\\' + ' ' * (2 * n - i) + '\n'

    for i in range(n - 1):
        crib_string += '|' + ' ' * (6 * n - 1) + '|\n'
    crib_string += '|' + ' ' * (2 * n) + '_' * (2 * n - 1) + ' ' * (2 * n) + '|\n'
    for i in range(n - 1):
        crib_string += '|' + ' ' * (2 * n - 1) + '|' + ' ' * (2 * n - 1) + '|' + ' ' * (2 * n - 1) + '|\n'
    crib_string += '|' + '_' * (2 * n - 1) + '|' + '_' * (2 * n - 1) + '|' + '_' * (2 * n - 1) + '|'

    return(crib_string)
