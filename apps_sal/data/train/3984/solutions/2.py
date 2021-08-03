def tacofy(word):
    ingred = {
        'a': 'beef', 'u': 'beef', 'i': 'beef', 'o': 'beef', 'e': 'beef',
        't': 'tomato', 'c': 'cheese', 'l': 'lettuce', 'g': 'guacamole', 's': 'salsa'
    }
    return ['shell'] + [ingred[c] for c in word.lower() if c in ingred] + ['shell']
