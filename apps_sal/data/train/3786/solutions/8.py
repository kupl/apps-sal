def siegfried(week, txt):
    symbols = [' ', '.', '!', '-', '\n']
    if week >= 1:
        rules = [['ci', 'si'], ['Ci', 'Si'], ['ce', 'se'], ['Ce', 'Se'], ['ch', '$$'], ['Ch', '$%'], ['c', 'k'], ['C', 'K'], ['$$', 'ch'], ['$%', 'Ch']]
        for translation in rules:
            txt = txt.replace(translation[0], translation[1])
    if week >= 2:
        rules = [['ph', 'f'], ['Ph', 'F']]
        for translation in rules:
            txt = txt.replace(translation[0], translation[1])
    if week >= 3:
        for (position, letter) in enumerate(txt):
            if letter == 'e' and position == len(txt) - 1 and (txt[position - 2] not in symbols) and (txt[position - 3] not in symbols):
                txt = txt[:position] + '$'
            elif letter == 'e' and position not in [0, 1, 2, len(txt) - 1] and (txt[position + 1] in symbols) and (txt[position - 2] not in symbols) and (txt[position - 3] not in symbols):
                txt = txt[:position] + '$' + txt[position + 1:]
        txt = txt.replace('$', '')
        for (position, letter) in enumerate(txt):
            if txt[position].lower() == txt[position - 1].lower() and position != 0 and letter.isalpha() and (letter not in symbols):
                txt = txt[:position] + '$' + txt[position + 1:]
        txt = txt.replace('$', '')
    if week >= 4:
        rules = [['th', 'z'], ['Th', 'Z'], ['wr', 'r'], ['Wr', 'R'], ['wh', 'v'], ['Wh', 'V'], ['w', 'v'], ['W', 'V']]
        for translation in rules:
            txt = txt.replace(translation[0], translation[1])
    if week >= 5:
        rules = [['ou', 'u'], ['Ou', 'U'], ['an', 'un'], ['An', 'Un']]
        for translation in rules:
            txt = txt.replace(translation[0], translation[1])
        for (position, letter) in enumerate(txt):
            if letter == 'i' and position == len(txt) - 3 and (txt[position + 1] == 'n') and (txt[position + 2] == 'g'):
                txt = txt[:position + 2] + '$' + txt[position + 3:]
            elif letter == 'i' and txt[position + 1] == 'n' and (txt[position + 2] == 'g') and (txt[position + 3] in symbols):
                txt = txt[:position + 2] + '$' + txt[position + 3:]
        txt = txt.replace('$', 'k')
        for (position, letter) in enumerate(txt):
            if letter == 'S' and txt[position + 1] == 'm' and (txt[position - 1] in symbols or position == 0):
                txt = txt[:position] + '$$' + txt[position + 2:]
        txt = txt.replace('$$', 'Schm')
    return txt
