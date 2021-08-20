def duplicate_encode(word):
    word = word.lower()
    dict = {}
    for char in word:
        dict[char] = ')' if char in dict else '('
    return ''.join((dict[char] for char in word))
