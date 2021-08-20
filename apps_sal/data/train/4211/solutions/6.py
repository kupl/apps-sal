def validate_word(word):
    word = word.lower()
    c_count = word.count(word[0])
    for c in word:
        if word.count(c) != c_count:
            return False
    return True
