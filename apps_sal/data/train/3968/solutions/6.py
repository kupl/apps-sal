def tail_swap(strings):
    s = [x.split(':') for x in strings]
    return [s[0][0] + ':' + s[1][1], s[1][0] + ':' + s[0][1]]
