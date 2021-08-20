table = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'bcdEfghIjklmnOpqrstUvwxyzA')


def changer(stg):
    return stg.lower().translate(table)
