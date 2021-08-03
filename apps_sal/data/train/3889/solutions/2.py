def area_code(text):
    return text[text.index('(') + 1:text.index(')')]
