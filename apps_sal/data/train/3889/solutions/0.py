def area_code(text):
    return text[text.find("(") + 1:text.find(")")]
