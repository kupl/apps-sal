import string


def words_to_marks(s):
    return sum((string.ascii_lowercase.index(x) + 1 for x in s))
