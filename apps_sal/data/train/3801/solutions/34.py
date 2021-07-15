def words_to_marks(s):
    abc = " abcdefghijklmnopqrstuvwxyz"
    return sum([abc.index(let) for let in s])    

