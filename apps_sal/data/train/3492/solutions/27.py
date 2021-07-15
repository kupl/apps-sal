def correct_polish_letters(st): 
    letters_dict = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    eng_string = ''
    for letter in st:
        if letter in letters_dict.keys():
            eng_string += letters_dict[letter]
        else:
            eng_string += letter
    return eng_string
