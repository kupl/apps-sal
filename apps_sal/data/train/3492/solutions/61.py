def correct_polish_letters(st):
    alphabet = {
        "ą": "a",
        "ć": "c",
        "ę": "e",
        "ł": "l",
        "ń": "n",
        "ó": "o",
        "ś": "s",
        "ź": "z",
        "ż": "z",
    }
    new_str = ''
    for c in list(st):
        if c in alphabet:
            new_str += alphabet[c]
        else:
            new_str += c
    return new_str
