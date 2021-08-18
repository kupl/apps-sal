def is_anagram(test, original):

    t = sorted(test.lower())
    o = sorted(original.lower())

    if t == o:
        print('true')
        return True
    else:
        print('false')
        return False
