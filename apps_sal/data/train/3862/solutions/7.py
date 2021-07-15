mirror=lambda c,a='abcdefghijklmnopqrstuvwxyz':c.lower().translate(str.maketrans(a,a[::-1]))
