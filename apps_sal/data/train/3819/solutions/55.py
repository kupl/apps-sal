def smash(words):
    # Begin here
    output = ''

    for word in words:
        output += word
        output += ' '

    return output[:-1]
