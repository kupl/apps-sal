def permutation_position(x):
    return sum((ord(c)-97)*26**p for p,c in enumerate(x[::-1]))+1
