def smash(words):
    if words == []:
        return ''
    else:
        i = 1
        word = words[0]
        while i < len(words):
            word = word + ' ' + words[i]
            i += 1
        return word
