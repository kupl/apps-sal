def esrever(s):
    return s and " ".join(x[::-1] for x in reversed(s[:-1].split())) + s[-1]
