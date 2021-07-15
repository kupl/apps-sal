DCT = {'t': 'tomato', 'l': 'lettuce', 'c': 'cheese', 'g': 'guacamole', 's': 'salsa'}
DCT.update({c:'beef' for c in "aeiuo"})

def tacofy(word):
    return ['shell'] + [DCT[c] for c in word.lower() if c in DCT] + ['shell']
