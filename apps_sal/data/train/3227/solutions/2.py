def to_lover_case(strng):
    from string import ascii_lowercase as a_l
    
    abc_to = "LOVE"*6 + "LO"

    return strng.lower().translate(str.maketrans(a_l, abc_to))
