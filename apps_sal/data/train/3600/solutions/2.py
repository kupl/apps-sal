def move_vowels(i): 
    s, v = '', ''
    for letter in i:
        if letter in 'aeiou': v+=letter
        else: s+=letter
    return s+v

