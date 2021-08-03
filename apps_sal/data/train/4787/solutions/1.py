def remove(s):
    return ''.join(sorted(s, key=lambda a: a == '!'))
