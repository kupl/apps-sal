def is_anagram(test, original):
    if len(original) != len(test):
        return False
    test = test.lower()
    original = original.lower()
    for letter in original:
        if original.count(letter) != test.count(letter):
            return False
    return True
