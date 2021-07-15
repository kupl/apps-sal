abc = "abcdefghijklmnopqrstuvwxyz"
trans = dict(zip(abc + abc.upper(), reversed(abc.upper() + abc)))

def decode(s):
    return "".join(trans.get(c, c) for c in s) if type(s) == str else "Input is not a string"
