def kebabize(string):
    return ''.join((list(map(transponse_char, string)))).lstrip('-')

def transponse_char(char):
    if char.isdigit():
        return ''
    if char.isupper():
        return '-{}'.format(char.lower())
    return char
