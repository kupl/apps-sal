from collections import Counter as C


def is_anagram(test, original):
    return C(test.lower()) == C(original.lower())
