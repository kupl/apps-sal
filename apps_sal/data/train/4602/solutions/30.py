def is_anagram(test, original):
    if len(test) != len(original):
        return False
    letters = {}
    for i in test.lower():
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    for i in original.lower():
        if i not in letters:
            return False
        if original.lower().count(i) != letters[i]:
            return False
    return True
