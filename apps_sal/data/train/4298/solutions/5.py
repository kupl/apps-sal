def n00bify(text):
    noobtext = marks(caps(add(replace(text))))
    return noobtext


def replace(text):
    text = text.replace(',', '').replace('.', '').replace("'", '').replace('too', '2').replace('Too', '2').replace('TOo', '2').replace('TOO', '2').replace('to', '2').replace('To', '2').replace('TO', '2').replace('fore', '4').replace('Fore', '4').replace('FOre', '4').replace('FORE', '4').replace('for', '4').replace('For', '4').replace('FOr', '4').replace('FOR', '4').replace('oo', '00').replace('Oo', '00').replace('OO', '00').replace('be', 'b').replace('are', 'r').replace('you', 'u').replace('please', 'plz').replace('people', 'ppl').replace('really', 'rly').replace('have', 'haz').replace('know', 'no').replace('Be', 'B').replace('Are', 'R').replace('You', 'U').replace('Please', 'Plz').replace('People', 'Ppl').replace('Really', 'Rly').replace('Have', 'Haz').replace('Know', 'No').replace('s', 'z').replace('S', 'Z')
    return text


def add(text):
    if text.startswith('w') or text.startswith('W'):
        text = 'LOL ' + text
    if len(text) - text.count('?') - text.count('!') >= 32:
        if text.startswith('LOL'):
            text = text.replace('LOL', 'LOL OMG')
        else:
            text = 'OMG ' + text
    return text


def caps(text):
    if text.startswith('h') or text.startswith('H'):
        text = text.upper()
    else:
        words = text.split()
        for i in range(1, len(words), 2):
            words[i] = words[i].upper()
        text = ' '.join(words)
    return text


def marks(text):
    num_words = len(text.split())
    text = text.replace('?', '?' * num_words)
    einself = ''
    for i in range(0, num_words):
        add = '!' if i % 2 == 0 else '1'
        einself = einself + add
    text = text.replace('!', einself)
    return text
