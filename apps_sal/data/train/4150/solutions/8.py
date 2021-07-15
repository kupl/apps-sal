def rot13c(c):
    if c.islower(): a = 'a'
    elif c.isupper(): a = 'A'
    else: return c
    return chr(ord(c)+13) if ord(c) < ord(a)+13 else chr(ord(c)-13)
def rot13(message): return ''.join(rot13c(c) for c in message)

