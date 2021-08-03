def move_vowels(input):
    non_vowels = input.translate(str.maketrans('', '', 'aeiou'))
    vowels = input.translate(str.maketrans('', '', non_vowels))
    return non_vowels + vowels
