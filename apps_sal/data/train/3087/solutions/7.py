def solve(stg):
    if is_pal(stg):
        return 'OK'
    if any((is_pal(f'{stg[:i]}{stg[i + 1:]}') for i in range(len(stg) + 1))):
        return 'remove one'
    return 'not possible'


def is_pal(stg):
    return stg == stg[::-1]
