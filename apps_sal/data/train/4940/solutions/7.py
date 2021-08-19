def eating(field):
    if 'H' in field:
        field = field.replace('A', '.')
        field = field.replace('V', '.')
    if 'R' in field:
        field = field.replace('V', '.')
    return field


def runing(field):
    field = field.replace('H', '.')
    field = field.replace('C', '.')
    field = field.replace('R', '.')
    return field


def shut_the_gate(farm):
    splited = farm.split('|')
    splited = [eating(item) for item in splited]
    if not farm.startswith('|') and (not farm.endswith('|')):
        if 'H' in splited[0] or 'H' in splited[-1]:
            splited[0] = splited[0].replace('A', '.')
            splited[0] = splited[0].replace('V', '.')
            splited[-1] = splited[-1].replace('A', '.')
            splited[-1] = splited[-1].replace('V', '.')
        if 'R' in splited[0] or 'R' in splited[-1]:
            splited[0] = splited[0].replace('V', '.')
            splited[-1] = splited[-1].replace('V', '.')
    if not farm.startswith('|'):
        splited[0] = runing(splited[0])
    if not farm.endswith('|'):
        splited[-1] = runing(splited[-1])
    return '|'.join(splited)
