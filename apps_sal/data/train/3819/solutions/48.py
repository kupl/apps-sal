def smash(words):
    result = ''
    for i in range(len(words)):
        if i < len(words) - 1:
            result += words[i] + ' '
        else:
            result += words[i]
    return result
