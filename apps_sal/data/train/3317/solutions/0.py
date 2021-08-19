def gr33k_l33t(string):
    gl = {'a': 'α', 'b': 'β', 'd': 'δ', 'e': 'ε', 'i': 'ι', 'k': 'κ', 'n': 'η', 'o': 'θ', 'p': 'ρ', 'r': 'π', 't': 'τ', 'u': 'μ', 'v': 'υ', 'w': 'ω', 'x': 'χ', 'y': 'γ'}
    return ''.join([gl.get(letter, letter) for letter in string.lower()])
