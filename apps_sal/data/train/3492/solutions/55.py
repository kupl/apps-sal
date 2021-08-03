def correct_polish_letters(st):
    letters = {
        "ą": "a",
        "ć": "c",
        "ę": "e",
        "ł": "l",
        "ń": "n",
        "ó": "o",
        "ś": "s",
        "ź": "z",
        "ż": "z"
    }
    result = ""
    for i in st:
        if i in letters:
            result += letters[i]
        else:
            result += i
    return result
