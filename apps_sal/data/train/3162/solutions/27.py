def compare(s1, s2):
    def upper_basis_ord(x): return sum(ord(c) for c in x.upper()) if type(x) == str and x.isalpha() else ''
    return upper_basis_ord(s1) == upper_basis_ord(s2)
