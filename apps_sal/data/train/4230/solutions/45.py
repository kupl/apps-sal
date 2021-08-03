import string


def reverse_letter(string):
    phrase = []
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in string:
        if letter in alpha:
            phrase.append(letter)
    return ''.join(reversed(phrase))


reverse_letter('hello')
