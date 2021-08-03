def position(alphabet):
    alphabet.lower()
    al = 'abcdefghijklmnopqrstuvwxyz'
    ind = al.index(alphabet)
    return "Position of alphabet: {}".format(ind + 1)
