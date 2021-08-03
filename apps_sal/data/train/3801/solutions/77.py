from string import ascii_lowercase


def words_to_marks(s):
    abc = ' ' + ascii_lowercase
    return sum(abc.index(char) for char in s)
