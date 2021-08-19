def tail_swap(strings):
    ((h1, t1), (h2, t2)) = (s.split(':') for s in strings)
    return [f'{h1}:{t2}', f'{h2}:{t1}']
