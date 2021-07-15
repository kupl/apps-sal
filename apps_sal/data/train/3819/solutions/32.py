def smash(words):
    x = []
    if words == []:
        return ''
    else:
        for i in range(len(words)-1):
            x.append(words[i] + ' ')
        x.append(words[len(words)-1])
        return ''.join(x)

