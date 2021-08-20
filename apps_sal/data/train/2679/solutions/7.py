from string import ascii_lowercase


def hamster_me(code, message):
    (table, code_letters) = ({}, set(code))
    (current_index, current_letter) = (0, '')
    for letter in ascii_lowercase * 2:
        if letter in code_letters:
            (current_index, current_letter) = (0, letter)
        current_index += 1
        table[letter] = current_letter + str(current_index)
    return ''.join(map(table.get, message))
