def correct_polish_letters(st):
    let = {
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
    new = ""
    for i in st:
        if i in let:
            new += let[i]
        else:
            new += i

    return new
