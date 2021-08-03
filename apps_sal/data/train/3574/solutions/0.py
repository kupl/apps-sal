def Dragon(n):
    if not isinstance(n, int) or n < 0:
        return ''

    value = 'Fa'

    for i in range(n):
        value = value.replace('a', 'aRcFR')
        value = value.replace('b', 'LFaLb')
        value = value.replace('c', 'b')

    return value.replace('a', '').replace('b', '')
