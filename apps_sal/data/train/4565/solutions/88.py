def replace_dots(str):
    change = '.'
    for element in str:
        if element in change:
            str = str.replace(element, '-')
    return str
