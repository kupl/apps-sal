def nerdify(txt):
    new_txt = ''
    for letter in txt:
        if letter == 'a' or letter == 'A':
            new_txt += '4'
        elif letter == 'e' or letter == 'E':
            new_txt += '3'
        elif letter == 'l':
            new_txt += '1'
        else:
            new_txt += letter
    return new_txt
