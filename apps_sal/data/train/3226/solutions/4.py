def land_perimeter(arr):
    a, b = ' '.join(arr), ' '.join(''.join(x) for x in zip(*arr))
    p = 4 * a.count('X') - 2 * 'O{}O{}O'.format(a, b).split('X').count('')
    return 'Total land perimeter: {}'.format(p)
