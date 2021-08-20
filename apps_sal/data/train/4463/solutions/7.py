def alphabet_position(text):
    al = 'abcdefghijklmnopqrstuvwxyz'
    return ' '.join(filter(lambda a: a != '0', [str(al.find(c) + 1) for c in text.lower()]))
