def stringy(size):
    x = True
    s = ''
    while size > 0:
        s += str(int(x))
        x = not x
        size -= 1
    return s
