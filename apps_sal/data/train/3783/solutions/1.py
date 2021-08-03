def frame(text, char):
    n = len(max(text, key=len)) + 4
    return "\n".join([char * n] +
                     ["%s %s %s" % (char, line.ljust(n - 4), char) for line in text] +
                     [char * n])
