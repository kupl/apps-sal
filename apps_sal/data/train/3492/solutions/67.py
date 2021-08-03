ALPHABET = {"ą": "a",
            "ć": "c",
            "ę": "e",
            "ł": "l",
            "ń": "n",
            "ó": "o",
            "ś": "s",
            "ź": "z",
            "ż": "z"}


def correct_polish_letters(st):

    result = ""
    for char in st:
        if (char in ALPHABET):
            result += ALPHABET[char]
        else:
            result += char

    return result
