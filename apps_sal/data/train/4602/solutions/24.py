def is_anagram(test, original):

    return ''.join(sorted(test.lower())) == ''.join(sorted(original.lower()))
