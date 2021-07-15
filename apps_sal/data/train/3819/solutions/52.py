def smash(words):
    string = ''
    for i in range(len(words)):
        if i == 0:
            string += words[0]
        else:
            string += ' ' + words[i]
    return string
        

