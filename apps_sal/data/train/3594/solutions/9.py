def is_isogram(word):
    try:
        word = word.lower()
        letters = [c for c in word if c.isalpha()]
        return len(set((word.count(c) for c in letters))) == 1
    except AttributeError:
        return False
