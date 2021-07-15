def encode(string):
    return ''.join(str(ord(i.lower()) - 96)  if i.isalpha() else i for i in string)
