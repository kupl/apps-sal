def move_vowels(input): 
    return "".join(sorted(input, key=lambda c: c in "aeiou"))
