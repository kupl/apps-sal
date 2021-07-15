def correct_polish_letters(st): 
    answer = ""
    d= {
        "ą":"a",
        "ć":"c",
        "ę":"e",
        "ł":"l",
        "ń":"n",
        "ó":"o",
        "ś":"s",
        "ź":"z",
        "ż":"z"
    }
    lst = ["ą","ć","ę","ł","ń","ó","ś","ź","ż"]
    
    for c in st:
        if c in lst:
            answer += d.get(c)
        else: 
            answer += c
    return answer
