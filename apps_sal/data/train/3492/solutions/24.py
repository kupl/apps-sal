def correct_polish_letters(st):
    polish = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']
    changeTo = ['a', 'c', 'e', 'l', 'n', 'o', 's', 'z', 'z']
    converted = []
    for letter in st:
        if letter in polish:
            i = polish.index(letter)
            converted.append(changeTo[i])
        else:
            converted.append(letter)
    return ''.join(converted)
