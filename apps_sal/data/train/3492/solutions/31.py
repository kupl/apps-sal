def correct_polish_letters(text): 
    x = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    
    for key in list(x.keys()):
        text = text.replace(key, str(x[key]))
    return text
  

