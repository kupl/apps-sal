import re


def remove_chars(string):
    """Pattern is anything BUT a-zA-Z and whitespace """
    pattern = '[^a-zA-Z\\s]'
    newstr = re.sub(pattern, '', string)
    return newstr
