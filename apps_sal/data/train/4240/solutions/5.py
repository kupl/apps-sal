def tongues(code):
    vowels = ['a', 'i', 'y', 'e', 'o', 'u']
    consonants = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']
    result = ''
    for char in code:
        uppercase = True if char.isupper() else False
        if char.lower() in vowels:
            new_char = vowels[(vowels.index(char.lower()) + 3) % len(vowels)]
        elif char.lower() in consonants:
            new_char = consonants[(consonants.index(char.lower()) + 10) % len(consonants)]
        else:
            new_char = char
        result += new_char.upper() if uppercase else new_char
    return result
