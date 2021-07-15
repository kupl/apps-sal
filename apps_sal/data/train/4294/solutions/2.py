def remove(text, what):
    for char, count in list(what.items()):
        text = "".join(text.split(char, count))
    return text

