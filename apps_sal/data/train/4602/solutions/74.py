def is_anagram(test, original):
    a = sorted(list(test.lower()))
    b = sorted(list(original.lower()))
    if a == b:
        print(f'The word {test} is an anagram of {original}')
        return True
    else:
        print(f'Characters do not match for test case {test}, {original}')
        return False
