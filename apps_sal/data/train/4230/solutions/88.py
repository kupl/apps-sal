def reverse_letter(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reversed_word = list()
    for letter in string:
        if letter in alphabet:
            reversed_word.append(letter)
    reversed_word.reverse()
    return "".join(reversed_word)
