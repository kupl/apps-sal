def trigrams(phrase):
    svar = ''
    if len(phrase) < 3:
        return ''
    else:
        phrase = phrase.replace(' ', '_')
        for i in range(len(phrase) - 2):
            svar = svar + ' ' + phrase[i:i + 3]
        return svar[1:]
