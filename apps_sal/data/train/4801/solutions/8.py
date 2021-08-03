legacy = {
    'cobol': 1000, 'nonobject': 500, 'monolithic': 500, 'fax': 100,
    'modem': 100, 'thickclient': 50, 'tape': 50, 'floppy': 50, 'oldschoolit': 50
}


def roast_legacy(workloads):
    comp = 0
    for w in ['slow!', 'expensive!', 'manual!', 'down!', 'hostage!', 'security!']:
        comp += workloads.lower().count(w)
    s = 0
    for k, v in legacy.items():
        s += workloads.lower().count(k) * v
    if comp == s == 0:
        return 'These guys are already DevOps and in the Cloud and the business is happy!'
    return 'Burn baby burn disco inferno {} points earned in this roasting and {} complaints resolved!'.format(s, comp)
