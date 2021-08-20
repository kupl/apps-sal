def next_letter(string):
    return ''.join((chr(ord(c) + (-25 if c in 'zZ' else 1)) if c.isalpha() else c for c in string))
