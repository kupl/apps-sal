trans_table = str.maketrans('abcdefghijklmnopqrstuvwxyz',
                            '0123456789abcdefghijklmnop')


def permutation_position(perm):
    return int(perm.translate(trans_table), 26) + 1
