def smash(words):
    output = ''
    for (idx, w) in enumerate(words):
        output = output + ' ' + words[idx]
    output = output.strip()
    return output
