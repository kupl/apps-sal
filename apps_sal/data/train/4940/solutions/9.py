import re


def shut_the_gate(farm):
    yards = farm.split('|')
    if len(yards) > 1:
        n = len(yards[0])
        yards[-1] += yards[0]
    for (i, yard) in enumerate(yards):
        s = ''
        if 'H' in yard:
            s = 'AV'
        elif 'R' in yard:
            s = 'V'
        if i == len(yards) - 1:
            s += 'HCR'
        if s:
            yards[i] = re.sub('[' + s + ']', '.', yard)
    if len(yards) > 1 and n:
        yards[0] = yards[-1][-n:]
        yards[-1] = yards[-1][:-n]
    return '|'.join(yards)
