def change(stg):
    chars = set(stg.lower())
    return ''.join((str(int(c in chars)) for c in 'abcdefghijklmnopqrstuvwxyz'))
