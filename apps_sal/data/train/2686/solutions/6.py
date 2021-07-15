def changer(string):
    d = str.maketrans('abcdefghijklmnopqrstuvwxyz',
                      'bcdEfghIjklmnOpqrstUvwxyzA')
    return string.lower().translate(d)
