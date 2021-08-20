def correct_polish_letters(st):
    dict = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    output = ''
    for x in st:
        if x in dict:
            output += dict[x]
        else:
            output += x
    return output
