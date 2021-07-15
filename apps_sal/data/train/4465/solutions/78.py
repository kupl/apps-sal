def super_size(n):
    sort_numbers = sorted(str(n))
    sort_numbers.reverse()
    return int(''.join(map(str,sort_numbers)))
