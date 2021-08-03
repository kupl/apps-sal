def remove(text, what):
    for c, v in what.items():
        text = text.replace(c, '', v)
    return text
