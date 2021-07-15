def first_non_repeated(s):
    for character in s:
        if s.count(character) == 1:
            return character
            break
