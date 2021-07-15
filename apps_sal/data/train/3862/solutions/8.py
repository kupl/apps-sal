mirror=lambda s,a='abcdefghijklmnopqrstuvwxyz':s.lower().translate(a.maketrans(a,a[::-1]))
