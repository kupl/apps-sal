import re
legcom = {'cobol': 1000, 'nonobject': 500, 'monolithic': 500, 'fax': 100, 'modem': 100, 'thickclient': 50, 'tape': 50, 'floppy': 50, 'oldschoolit': 50, 'slow!': 1j, 'expensive!': 1j, 'manual!': 1j, 'down!': 1j, 'hostage!': 1j, 'security!': 1j}
lcre = re.compile('|'.join(map(re.escape, list(legcom.keys()))), flags=re.I)


def roast_legacy(ws):
    s = sum((legcom[m.group().lower()] for m in lcre.finditer(ws)))
    return 'Burn baby burn disco inferno {} points earned in this roasting and {} complaints resolved!'.format(int(s.real), int(s.imag)) if s else 'These guys are already DevOps and in the Cloud and the business is happy!'
