digits = 'zero one two three four five six seven eight nine'.split()


def uncollapse(stg):
    for d in digits:
        stg = stg.replace(d, f'{d} ')
    return stg.strip()
