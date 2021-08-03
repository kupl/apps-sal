import re


def roast_legacy(s):
    cpn = len(re.findall(r'slow!|expensive!|manual!|down!|hostage!|security!', s, re.I))
    points = list(map(lambda x: x.lower(), re.findall(r'COBOL|nonobject|monolithic|fax|modem|thickclient|tape|floppy|oldschoolIT', s, re.I)))
    p = sum([[[50, 100][i[:2] in 'fa mo'], 500]['no' in i], 1000][i[0] == 'c'] for i in points)
    return f'Burn baby burn disco inferno {p} points earned in this roasting and {cpn} complaints resolved!' if p or cpn else \
           'These guys are already DevOps and in the Cloud and the business is happy!'
