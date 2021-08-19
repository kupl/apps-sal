import re


def n00bify(text):
    replacementArray = [('too', '2'), ('to', '2'), ('fore', '4'), ('for', '4'), ('oo', '00'), ('be', 'b'), ('are', 'r'), ('you', 'u'), ('please', 'plz'), ('people', 'ppl'), ('really', 'rly'), ('have', 'haz'), ('know', 'no'), ('\\.', ''), (',', ''), ("\\'", '')]
    firstLetterW = re.match('^w', text, flags=re.IGNORECASE)
    firstLetterH = re.match('^h', text, flags=re.IGNORECASE)
    for x in replacementArray:
        text = re.sub(x[0], x[1], text, flags=re.IGNORECASE)
    text = text.replace('s', 'z')
    text = text.replace('S', 'Z')
    count = 0
    for c in text:
        if (c.isalpha() or c.isdigit()) or c == ' ':
            count += 1
    if firstLetterW and count >= 28:
        text = 'LOL OMG ' + text
    elif firstLetterW:
        text = 'LOL ' + text
    elif count >= 32:
        text = 'OMG ' + text
    wordList = text.split()
    for i in range(len(wordList)):
        if i % 2 == 1 or firstLetterH:
            wordList[i] = wordList[i].upper()
    text = ' '.join(wordList)
    text = text.replace('?', '?' * len(wordList))
    text = text.replace('!', exclamation(len(wordList)))
    return text


def exclamation(n):
    exclams = '!1' * (n // 2)
    if n % 2 == 1:
        exclams = exclams + '!'
    return exclams
