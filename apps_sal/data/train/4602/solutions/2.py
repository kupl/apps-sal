from collections import Counter
# write the function is_anagram
def is_anagram(test, original):
    return Counter(test.lower()) == Counter(original.lower())
