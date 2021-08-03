def capitalize(s):
    return [''.join([char.lower() if i % 2 == 1 else char.upper() for i, char in enumerate(s)]), ''.join([char.lower() if i % 2 == 0 else char.upper() for i, char in enumerate(s)])]
