from string import ascii_lowercase


def words_to_marks(s):
    return sum((ascii_lowercase.index(i) + 1 for i in s))
