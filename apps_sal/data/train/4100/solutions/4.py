def reverse_alternate(s):
    words = s.split()
    words[1::2] = [word[::-1] for word in words[1::2]]
    return ' '.join(words)
