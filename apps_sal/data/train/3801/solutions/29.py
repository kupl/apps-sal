def words_to_marks(s):
    alpha = '0abcdefghijklmnopqrstuvwxyz'
    return sum(alpha.find(char) for char in s)
