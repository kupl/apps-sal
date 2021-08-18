def smash(words):
    output = ''

    for word in words:
        output += word
        output += ' '

    return output[:-1]
