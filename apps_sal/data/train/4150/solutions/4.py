def rot13(message):
    root13in = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    root13out = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    root13map = dict(zip(root13in, root13out))
    res = ''.join([root13map.get(s, s) for s in message])
    return res
