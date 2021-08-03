def area_code(text):
    parenth1 = text.find('(')
    parenth2 = text.find(')')
    return text[parenth1 + 1:parenth2]
