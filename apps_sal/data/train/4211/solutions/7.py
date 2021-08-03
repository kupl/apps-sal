def validate_word(word):
    word = word.lower()
    return all(word.count(i) == word.count(word[0]) for i in word)
