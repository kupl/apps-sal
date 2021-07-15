def reverseWords(s):
    x = s.split()
    y = x[::-1]
    z = " ".join(str(a) for a in y)
    return z
