import string


def position(alphabet):
    ab = dict(zip(string.ascii_lowercase, range(1, 27)))
    return f"Position of alphabet: {ab.get(alphabet)}"
