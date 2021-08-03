def get_free_urinals(urinals):
    if '11' in urinals:
        return -1
    return sum((len(s) - 1) // 2 for s in f'10{urinals}01'.split('1') if s)
