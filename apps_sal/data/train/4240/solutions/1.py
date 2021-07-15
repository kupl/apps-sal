vowels = 'aiyeou' * 2
vowels += vowels.upper()
consonants = 'bkxznhdcwgpvjqtsrlmf' * 2
consonants += consonants.upper()

def tongues(code):
    result = ""
    for c in code:
        if c in vowels:
            result += vowels[vowels.index(c) + 3]
        elif c in consonants:
            result += consonants[consonants.index(c) + 10]
        else:
            result += c
    return result
