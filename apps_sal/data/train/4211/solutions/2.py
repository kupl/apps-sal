def validate_word(word):
    word = word.lower()
    return len(set((word.count(c) for c in word))) == 1
