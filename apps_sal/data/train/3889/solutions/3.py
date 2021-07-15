def area_code(text):
    # Your code goes here
    area = text.find('(')
    return text[area+1:area+4]
