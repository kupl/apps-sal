def is_anagram(test, original):
    letterCount = dict.fromkeys('abcdefghijklmnopqrstuvwxyz', 0)

    for c in test.lower():
        letterCount[c] += 1

    for c in original.lower():
        letterCount[c] -= 1

    for value in list(letterCount.values()):
        if value != 0:
            return False

    return True
