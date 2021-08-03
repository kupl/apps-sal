def one_down(txt):
    if type(txt) != str:
        return "Input is not a string"
    return ''.join(chr(65 + (ord(i) - 66) % 26) if i.isupper() else chr(97 + (ord(i) - 98) % 26) if i.islower() else i for i in txt)
