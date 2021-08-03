def to_alternating_case(string):
    capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                       'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_string = []

    for character in string:
        if character in capital_letters:
            new_string.append(lowercase_letters[capital_letters.index(character)])
        if character in lowercase_letters:
            new_string.append(capital_letters[lowercase_letters.index(character)])
        if character not in capital_letters and character not in lowercase_letters:
            new_string.append(character)

    return ''.join(new_string)
