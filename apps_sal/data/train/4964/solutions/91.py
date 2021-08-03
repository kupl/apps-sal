import string


def is_uppercase(inp):
    return inp.isupper() and inp not in string.punctuation or inp.isnumeric()
