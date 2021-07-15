def words_to_marks(s):
    letters = list(s)
    word_value = 0
    sum_list = []
    dicti = {}
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for i in range(len(alphabet)):
        dict_ = {alphabet[i]: i}
        dicti.update(dict_)
    for j in letters:
        word_value += dicti[j] + 1
    return word_value

            

