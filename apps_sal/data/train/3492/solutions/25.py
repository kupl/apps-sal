def correct_polish_letters(st):
    trans = {"ą": "a", "ć": "c", "ę": "e", "ł": "l", "ń": "n", 
             "ó": "o", "ś": "s", "ź": "z", "ż": "z"}
    return "".join(trans.get(s, s) for s in st)
