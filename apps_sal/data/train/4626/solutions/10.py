from string import ascii_lowercase as lower, ascii_uppercase as upper

trans = str.maketrans(lower+upper, lower[::-1]+upper[::-1])

def decode(string_):
    try:
        return string_.translate(trans)
    except AttributeError:
        return "Input is not a string"
