def string_clean(s):
    remove_characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for character in remove_characters:
        s = s.replace(character, '')
    return s
