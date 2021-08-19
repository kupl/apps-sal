def tacofy(word):
    d = {'a': 'beef', 'e': 'beef', 'i': 'beef', 'o': 'beef', 'u': 'beef', 't': 'tomato', 'l': 'lettuce', 'c': 'cheese', 'g': 'guacamole', 's': 'salsa'}
    return ['shell'] + [d[i] for i in word.lower() if i in d] + ['shell']
