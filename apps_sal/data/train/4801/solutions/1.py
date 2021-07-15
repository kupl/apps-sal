complaints = ["slow!", "expensive!", "manual!", "down!", "hostage!", "security!"]
legacies = {
    "cobol": 1000,
    "nonobject": 500,
    "monolithic": 500,
    "fax": 100,
    "modem": 100,
    "thickclient": 50,
    "tape": 50,
    "floppy": 50,
    "oldschoolit": 50
}

def roast_legacy(workloads):
    wl = workloads.lower()
    comps = sum([wl.count(s) for s in complaints])
    score = sum([wl.count(s) * p for s, p in legacies.items()])
    
    if (comps, score) == (0, 0):
        return "These guys are already DevOps and in the Cloud and the business is happy!"
    return "Burn baby burn disco inferno {} points earned in this roasting and {} complaints resolved!".format(score, comps)
