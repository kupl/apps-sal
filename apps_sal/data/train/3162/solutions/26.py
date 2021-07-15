def compare(s1,s2):
    f = lambda s : all(c.lower() in 'abcdefghijklmnopqrstuvwxyz' for c in s)*sum(ord(c.upper()) for c in s) if s else False
    return f(s1)==f(s2)
