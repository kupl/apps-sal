def gr33k_l33t(s):
    doc = {'a': 'α', 'b': 'β', 'd': 'δ', 'e': 'ε', 'i': 'ι', 'k': 'κ', 'n': 'η', 'o': 'θ', 'p': 'ρ', 'r': 'π', 't': 'τ', 'u': 'μ', 'v': 'υ', 'w': 'ω', 'x': 'χ', 'y': 'γ'}
    return ''.join((doc.get(e, e) for e in s.lower()))
