def is_isogram(word):
    if type(word) != str or word == '':
        return False
    word = word.lower()
    cnts = [word.count(c) for c in word if c.isalpha()]
    return len(set(cnts)) == 1
