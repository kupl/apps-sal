dict = {'a': 'beef', 'e': 'beef', 'i': 'beef', 'o': 'beef', 'u': 'beef', 't': 'tomato', 'l': 'lettuce', 'c': 'cheese', 'g': 'guacamole', 's': 'salsa'}


def tacofy(word):
    outlist = ['shell']
    for c in word.lower():
        if c in dict:
            outlist.append(dict.get(c))
    outlist.append('shell')
    return outlist
