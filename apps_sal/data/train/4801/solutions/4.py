import re

legacy = {
    "cobol": 1000,
    "nonobject": 500,
    "monolithic": 500,
    "fax": 100,
    "modem": 100,
    "thickclient": 50,
    "tape": 50,
    "floppy": 50,
    "oldschoolit": 50,
}
legacy_pattern = re.compile('|'.join(legacy))
complaint_pattern = re.compile('slow|expensive|manual|down|hostage|security')

def roast_legacy(workloads):
    w = workloads.replace('-', '').lower()
    complaints = sum(1 for _ in complaint_pattern.finditer(w))
    points = sum(legacy[match.group()] for match in legacy_pattern.finditer(w))
    if complaints or points:
        return f'Burn baby burn disco inferno {points} points earned in this roasting and {complaints} complaints resolved!'
    else:
        return 'These guys are already DevOps and in the Cloud and the business is happy!'
