from string import lowercase


def position(letter):
    return 'Position of alphabet: %d' % (
        1 + lowercase.index(letter))
