def tail_swap(strings):
    (a, b) = strings
    (a, b) = (a.split(':'), b.split(':'))
    return [f'{a[0]}:{b[1]}', f'{b[0]}:{a[1]}']
