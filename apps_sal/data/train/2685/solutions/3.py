keyword_cipher = lambda m, k, s='abcdefghijklmnopqrstuvwxyz': m.lower().translate(str.maketrans(s, ''.join(sorted(set(k), key=k.index) + [i for i in s if i not in k])))
