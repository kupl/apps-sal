def correct_polish_letters(st):
    PolishDict = {
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
    newStr = ""
    for i in range(len(st)):
        if st[i] in PolishDict:
            newStr += PolishDict[st[i]]
        else:
            newStr += st[i]
    return newStr
