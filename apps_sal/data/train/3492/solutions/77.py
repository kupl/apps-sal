def correct_polish_letters(st): 
    res = ""
    
    letters = { "ą": "a", "ć":  "c", "ę":  "e", "ł":  "l", "ń":  "n", 
                "ó":  "o", "ś":  "s", "ź":  "z", "ż": "z" }
    
    for elem in st:
        for letter in elem:
            if letter in letters:
                res += letters[letter]
            else:
                res += elem
    
    return res               
