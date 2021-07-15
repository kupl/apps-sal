def words_to_marks(s):
    abc = "abcdefghijklmnopqrstuvwxyz"
    result = 0
    for letter in s:
        result+=abc.index(letter)+1
    
    return result
