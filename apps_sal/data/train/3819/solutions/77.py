def smash(words):
    text = ''
    for i in words:
        text += i
        if i != words[-1]:
            text += ' '
    return text

