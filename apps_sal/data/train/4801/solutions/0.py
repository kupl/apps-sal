import re
complaints = ['slow!', 'expensive!', 'manual!', 'down!', 'hostage!', 'security!']
legacy = {'cobol': 1000, 'nonobject': 500, 'monolithic': 500, 'fax': 100, 'modem': 100, 'thickclient': 50, 'tape': 50, 'floppy': 50, 'oldschoolit': 50}


def roast_legacy(workloads):
    complaining = sum((1 for _ in re.finditer('|'.join(complaints), workloads.lower())))
    roasting = sum((legacy[m.group()] for m in re.finditer('|'.join(legacy), workloads.lower())))
    if roasting or complaining:
        return 'Burn baby burn disco inferno %d points earned in this roasting and %d complaints resolved!' % (roasting, complaining)
    else:
        return 'These guys are already DevOps and in the Cloud and the business is happy!'
