import re


def encoder(data):
    dct = {'': 0}
    search = ''
    output = ''
    for i in range(len(data)):
        search += data[i]
        if search not in dct:
            dct[search] = len(dct)
            output += f'{dct[search[:-1]]}{search[-1]}'
            search = ''
        try:
            search + data[i + 1]
        except IndexError:
            if search == data[-len(search):]:
                output += f'{dct[search]}'
    return output


def decoder(data):
    dct = {0: ''}
    output = ''
    lsnb = re.findall('\\d+', data)
    lsch = re.findall('[A-Z]', data)
    for i in range(len(lsnb)):
        try:
            lsch[i]
            dct[len(dct)] = dct[int(lsnb[i])] + lsch[i]
            output += dct[len(dct) - 1]
        except IndexError:
            output += dct[int(lsnb[i])]
    return output
