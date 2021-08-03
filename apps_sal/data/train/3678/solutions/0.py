TABLE = str.maketrans('0123456789', '9876543210')


def code(*args):
    return sum(map(lambda n: int(str(n).translate(TABLE)), args))
