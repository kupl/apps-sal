def words_to_marks(s):
    abc = " abcdefghijklmnopqrstuvwxyz"
    return sum([abc.index(letter) for letter in s])
