PLAINTS = {"slow!", "expensive!", "manual!", "down!", "hostage!", "security!"}
LEGACY = {"cobol": 1000, "nonobject": 500, "monolithic": 500, "fax": 100, "modem": 100, "thickclient": 50, "tape": 50, "floppy": 50, "oldschoolit": 50}

def roast_legacy(workloads):
    workloads = workloads.lower()
    p = sum( workloads.count(elt) for elt in PLAINTS )
    l = sum( workloads.count(elt) * LEGACY[elt] for elt in LEGACY )
    return 'These guys are already DevOps and in the Cloud and the business is happy!' if p+l == 0 else 'Burn baby burn disco inferno {} points earned in this roasting and {} complaints resolved!'.format(l, p)
