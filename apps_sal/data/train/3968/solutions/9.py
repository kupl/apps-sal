def tail_swap(strings):
    a, b = [ele.split(':') for ele in strings]
    return [f'{a[0]}:{b[1]}', f'{b[0]}:{a[1]}']
