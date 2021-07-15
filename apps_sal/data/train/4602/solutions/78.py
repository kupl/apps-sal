# write the function is_anagram
def is_anagram(test, original):
    result = True if (len(test) == len(original)) else False
    for letter in test.upper():
        result = False if (letter not in original.upper()) else result
    return result
