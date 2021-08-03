def words_to_marks(s):
    words_value = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)
    word = list(s)
    letters_value = {}
    for i in range(len(alphabet)):
        dict_ = {alphabet[i]: i}
        letters_value.update(dict_)
    for j in word:
        words_value = words_value + letters_value[j] + 1
    print(words_value)
    return words_value


s = 'cat'
words_to_marks(s)
