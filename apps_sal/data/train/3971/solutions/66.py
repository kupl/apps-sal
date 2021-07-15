def tidyNumber(n):
    return int(''.join(sorted(f'{n}'))) == n
