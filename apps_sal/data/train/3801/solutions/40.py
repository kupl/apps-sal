import string
def words_to_marks(s):
    return sum([string.ascii_lowercase.find(x)+1 for x in s])
