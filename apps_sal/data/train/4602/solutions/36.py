def is_anagram(test, original):
    letters = [c for c in test.lower()]
    for char in original.lower():
        if char in letters:
            del letters[letters.index(char)]
        else:
            return False
    return not bool(len(letters))
