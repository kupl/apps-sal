from string import ascii_uppercase, ascii_lowercase

D = {c:str(i) for string in (ascii_uppercase, ascii_lowercase) for i,c in enumerate(string, 1)}

def encode(string):
    return ''.join(D.get(c, c) for c in string)
