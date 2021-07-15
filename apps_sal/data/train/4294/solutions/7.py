def remove(text, what):
    for k, v in what.items():
        text = text.replace(k, '', v)
    return text
