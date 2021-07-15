import re

EAT = {'H': 'AV', 'R': 'V'}

def shut_the_gate(farm):
    parts = farm.split('|')
    partsSets = list(map(set, parts))
    for i in range(len(parts)):
        isOut   = i in [0, len(parts)-1]
        inThere = set('RHC') & (partsSets[i] | (partsSets[len(parts)-1-i] if isOut else set()))
        toErase = ''.join(EAT.get(x,'') for x in inThere) + 'HCR'*isOut
        if toErase: parts[i] = re.sub(r'[{}]'.format(toErase), '.', parts[i])
    return '|'.join(parts)
