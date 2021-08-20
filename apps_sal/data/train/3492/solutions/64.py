def correct_polish_letters(st):
    letters_dict = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    result = ''
    for letter in st:
        if letter in letters_dict.keys():
            result += letters_dict[letter]
        else:
            result += letter
    return result
