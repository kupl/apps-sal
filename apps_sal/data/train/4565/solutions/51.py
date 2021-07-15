def replace_dots(string):
    while "." in string: string = string.replace(".", "-")
    return string
