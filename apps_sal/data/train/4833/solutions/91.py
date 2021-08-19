def replace_exclamation(s):
    return ''.join(({'a': '!', 'e': '!', 'i': '!', 'o': '!', 'u': '!', 'A': '!', 'E': '!', 'I': '!', 'O': '!', 'U': '!'}.get(e, e) for e in s))
