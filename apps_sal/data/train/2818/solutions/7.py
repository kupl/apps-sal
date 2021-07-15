def duplicate_encode(word):
    word = word.lower()
    return ''.join([')' if word.count(char) > 1 else '(' for char in word])
