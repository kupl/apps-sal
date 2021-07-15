low = 'zyxwvutsrqponmlkjihgfedcba'
up = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

def decode(s):
    if not isinstance(s, str): return "Input is not a string"
    return ''.join((low[ord(x)-97] if x.islower() else up[ord(x)-65]) if x.isalpha() else x for x in s)
