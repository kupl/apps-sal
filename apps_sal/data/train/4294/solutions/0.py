def remove(text, what):
    for char in what:
        text = text.replace(char,'',what[char])
    return text
