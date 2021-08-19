def contamination(text, char):
    if text == '':
        return text
    else:
        for letter in text:
            text = text.replace(letter, char)
        return text
