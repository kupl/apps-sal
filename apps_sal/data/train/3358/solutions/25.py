def correct(string):
    remap = {'5': 'S', '0': 'O', '1': 'I'}
    return ''.join((x.replace(x, remap[x]) if x in remap else x for x in list(string)))
