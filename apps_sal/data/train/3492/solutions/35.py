def correct_polish_letters(st):
    result = ""
    alphabet = {"ą": "a",
                "ć": "c",
                "ę": "e",
                "ł": "l",
                "ń": "n",
                "ó": "o",
                "ś": "s",
                "ź": "z",
                "ż": "z"}

    for n in st:
        if n in alphabet:
            result += alphabet[n]
        else:
            result += n

    return result
