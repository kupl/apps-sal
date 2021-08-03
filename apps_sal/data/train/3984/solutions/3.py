def tacofy(word):
    d = {'t': 'tomato', 'l': 'lettuce', 'c': 'cheese', 'g': 'guacamole', 's': 'salsa'}
    return ['shell'] + [d.get(i, 'beef') for i in word.lower() if i in 'aeioutlcgs'] + ['shell']
