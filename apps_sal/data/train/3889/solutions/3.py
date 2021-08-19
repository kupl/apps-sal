def area_code(text):
    area = text.find('(')
    return text[area + 1:area + 4]
