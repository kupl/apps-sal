# replace all vowels with exclamation marks [aeiouAEIOU]
# input - string
# output - string
# edge cases - empty strings, non alphanumeric characters

def replace_exclamation(s):
    # for e in string get element
    # if key in dict doesn't exist, return e
    # join list to return string
    return ''.join({'a': '!', 'e': '!', 'i': '!', 'o': '!', 'u': '!', 'A': '!', 'E': '!', 'I': '!', 'O': '!', 'U': '!'}.get(e, e) for e in s)
