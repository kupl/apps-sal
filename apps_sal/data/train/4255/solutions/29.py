def make_upper_case(word):
    new_word = ''
    for letter in word:
        if 97 <= ord(letter) <= 122:
            new_word += chr(ord(letter) - 32)
        else:
            new_word += letter
    return new_word
