def get_free_urinals(urinals):
    return -1 if '11' in urinals else sum(((len(l) - 1) // 2 for l in f'0{urinals}0'.split('1')))
