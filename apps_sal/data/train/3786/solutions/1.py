import re


def siegfried(week, txt):
    if week >= 1:
        txt = re.sub('c(?!h)', 'k', re.sub('C(?!h)', 'K', txt.replace('ci', 'si').replace('Ci', 'Si').replace('ce', 'se').replace('Ce', 'Se')))
    if week >= 2:
        txt = txt.replace('ph', 'f').replace('Ph', 'F')
    if week >= 3:
        txt = re.sub('([A-z]{2,})e([-!?]+)', '\\1\\2', ' '.join([x.rstrip('e') if len(x) > 3 else x for x in re.sub('([A-z])\\1', '\\1', txt, flags=re.I).split()]))
    if week >= 4:
        txt = txt.replace('th', 'z').replace('Th', 'Z').replace('wr', 'r').replace('Wr', 'R').replace('wh', 'v').replace('Wh', 'V').replace('w', 'v').replace('W', 'V')
    if week >= 5:
        txt = (' ' + txt + ' ').replace('ou', 'u').replace('Ou', 'U').replace('an', 'un').replace('An', 'Un').replace('ing ', 'ink ').replace(' sm', ' schm').replace(' Sm', ' Schm')
    return txt.strip()
