def compare(s1,s2):
    upper_basis_ord = lambda x: sum(ord(c) for c in x.upper()) if type(x) == str and x.isalpha() else ''
    return upper_basis_ord(s1) == upper_basis_ord(s2)
