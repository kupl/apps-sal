def word_to_bin(s):
    return list(map(lambda x: format(ord(x),'08b'),s))
