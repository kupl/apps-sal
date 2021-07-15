def tacofy(word):
    word = [i if i.lower() in 'tlcgs' else 'a' if i.lower() in 'aeiou' else '' for i in word ]
    d = {'a': 'beef', 't': 'tomato', 'l': 'lettuce', 'c': 'cheese', 'g': 'guacamole', 's': 'salsa'}
    return ['shell'] + [d[i.lower()] for i in word if i] + ['shell']
