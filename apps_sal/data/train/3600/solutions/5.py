def move_vowels(s):
    return "".join(sorted(s, key=lambda x: x in "aiueo"))
