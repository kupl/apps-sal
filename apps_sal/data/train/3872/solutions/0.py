def sort_it(list_, n):
    return ', '.join(sorted(list_.split(', '), key=lambda i: i[n - 1]))
