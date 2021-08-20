def contamination(text, char):
    large = 0
    newText = ''
    for letters in text:
        large += 1
    if text == '':
        newText == ''
    else:
        newText = large * char
    return newText
