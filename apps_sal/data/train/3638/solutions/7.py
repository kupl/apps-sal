from string import ascii_lowercase


def gematria(strng):
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 600, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 700, 900, 300, 400, 500]
    alphabet_values = {letter: num for num, letter in zip(values, ascii_lowercase)}
    return sum([alphabet_values[letter] if letter in ascii_lowercase else 0 for letter in strng.lower()])
