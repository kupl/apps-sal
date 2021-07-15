def stringy(size):
    # Good Luck!
    x = ''
    while size > len(x):
        x = x + '1'
        while size > len(x):
                x = x + '0'
                break
    return x
