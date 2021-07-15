from string import ascii_lowercase
def position(char):
    return "Position of alphabet: {0}".format(
        ascii_lowercase.index(char) + 1)
