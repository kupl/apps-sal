from string import ascii_lowercase


def solve(arr):
    return [[(string_letter == alphabet_letter) for string_letter, alphabet_letter
             in zip(i.lower(), ascii_lowercase)].count(True)
            for i in arr]
