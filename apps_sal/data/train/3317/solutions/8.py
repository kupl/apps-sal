a = {'A': 'α', 'B': 'β', 'D': 'δ', 'E': 'ε', 'I': 'ι', 'K': 'κ', 'N': 'η', 'O': 'θ', 'P': 'ρ', 'R': 'π', 'T': 'τ', 'U': 'μ', 'V': 'υ', 'W': 'ω', 'X': 'χ', 'Y': 'γ'}


def gr33k_l33t(string):
    b = list(string.upper())
    return ''.join([a[x] if x in a else x.lower() for x in b])
