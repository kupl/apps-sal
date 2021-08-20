import re


def increment_string(string):
    if bool(re.match('.*?([0-9]+)$', string)):
        numeros = str(int(re.match('.*?([0-9]+)$', string).group(1)) + 1).zfill(len(re.match('.*?([0-9]+)$', string).group(1)))
    else:
        numeros = str(1)
    if bool(re.match('(.*?)[0-9]*$', string)):
        letras = re.match('(.*?)[0-9]*$', string).group(1)
    else:
        letras = ''
    return letras + numeros
