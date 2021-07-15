def scramble(string_to_rearrange, string_to_match):
    letters_in_string_to_match = {}
    for letter in string_to_match:
        if letter not in letters_in_string_to_match:
            letters_in_string_to_match[letter] = string_to_match.count(letter)
    letters_in_string_to_rearrange = {}
    for letter in string_to_rearrange:
        if letter not in letters_in_string_to_rearrange:
            letters_in_string_to_rearrange[letter] = string_to_rearrange.count(letter)
    for letter in letters_in_string_to_match:
        try:
            if letters_in_string_to_match[letter] > letters_in_string_to_rearrange[letter]:
                return False
        except KeyError:
            return False
    return True

