def correct_polish_letters(st): 
    ls = {"ą": "a", "ć": "c", "ę": "e", "ł": "l", "ń": "n", "ó": "o", "ś": "s", "ź": "z", "ż": "z"}
    return ''.join(ls[l] if l in ls else l for l in st)

