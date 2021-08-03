# write the function is_anagram
def is_anagram(test, original):
    test = list(test.lower())
    original = list(original.lower())
    if len(test) != len(original):
        return False
    for word in test:
        for word2 in original:
            if word == word2:
                original.remove(word2)
                break
    if len(original) == 0:
        return True
    else:
        return False
