def tongues(code):
    vowels = {'a': 'e', 'i': 'o', 'y': 'u',
              'e': 'a', 'o': 'i', 'u': 'y'}
    consonants = {'b': 'p', 'k': 'v', 'x': 'j', 'z': 'q', 'n': 't',
                  'h': 's', 'd': 'r', 'c': 'l', 'w': 'm', 'g': 'f',
                  'p': 'b', 'v': 'k', 'j': 'x', 'q': 'z', 't': 'n',
                  's': 'h', 'r': 'd', 'l': 'c', 'm': 'w', 'f': 'g'}
    message = ''
    for char in code:
        Upper = False
        if char == char.upper():
            Upper = True
            char = char.lower()
        if char in vowels.keys():
            new_char = vowels[char]
        elif char in consonants.keys():
            new_char = consonants[char]
        else:
            new_char = char
        if Upper:
            new_char = new_char.upper()
        message += new_char
    return message
