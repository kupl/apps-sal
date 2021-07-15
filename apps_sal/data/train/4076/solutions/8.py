def get_count(words=""):
    vowels = consonants = 0
    if type(words) == str:
        for char in words.lower():
            if char.isalpha():
                vowel = char in "aeiou"
                vowels += vowel
                consonants += not vowel
    return {"vowels": vowels, "consonants": consonants}
