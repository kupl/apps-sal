def pig_latin(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = s.lower()
    if not word.isalpha():
        return None
    if word[0] in vowels:
        return word + 'way'
    for (i, letter) in enumerate(word):
        if letter in vowels:
            return word[i:] + word[:i] + 'ay'
    return word + 'ay'
