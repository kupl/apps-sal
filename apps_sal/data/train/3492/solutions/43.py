def correct_polish_letters(st):
    polish = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    new_string = ""
    for i in st:
        if i in polish:
            new_string += (polish[i])
        else:
            new_string += i
    return new_string
