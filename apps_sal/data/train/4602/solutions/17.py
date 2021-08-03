aprime = {'a': 2, 'c': 5, 'b': 3, 'e': 11, 'd': 7, 'g': 17, 'f': 13, 'i': 23, 'h': 19, 'k': 31,
          'j': 29, 'm': 41, 'l': 37, 'o': 47, 'n': 43, 'q': 59, 'p': 53, 's': 67, 'r': 61, 'u': 73, 't': 71,
          'w': 83, 'v': 79, 'y': 97, 'x': 89, 'z': 101}


def aprime_sum(str):
    strChList = list(str.lower())
    return sum([aprime[x] for x in strChList])

# write the function is_anagram


def is_anagram(test, original):
    if aprime_sum(test) == aprime_sum(original):
        return True
    else:
        return False
