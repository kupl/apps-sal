def correct_polish_letters(st):
    Polish_alphabet = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    result = ''
    for el in st:
        result += Polish_alphabet.get(el, el)
    return result
