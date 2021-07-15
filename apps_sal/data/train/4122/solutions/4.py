def sc(s):
    return ''.join(i for i in s if i.swapcase() in set(s))
