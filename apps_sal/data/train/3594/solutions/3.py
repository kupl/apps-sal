def is_isogram(word):
    if not (word and isinstance(word, str)):
        return False
    word = word.lower()
    return len(set(word.count(c) for c in set(word) if c.isalpha())) == 1

