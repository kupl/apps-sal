import string


def words_to_marks(s):
    return sum(map(string.ascii_lowercase.index, s)) + len(s)
