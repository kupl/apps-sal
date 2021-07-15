def move_vowels(input):
    return "".join(sorted(input, key="aeiou".__contains__))
