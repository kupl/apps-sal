def roast_legacy(workloads):
    points = {'cobol': 1000, 'nonobject': 500, 'monolithic': 500, 'fax': 100,
              'modem': 100, 'thickclient': 50, 'tape': 50, 'floppy': 50, 'oldschoolit': 50}
    complaints = ['slow!', 'expensive!', 'manual!', 'down!', 'hostage!', 'security!']

    work_loads = workloads.lower()

    count = sum(work_loads.count(complaint) for complaint in complaints)
    legacy = sum(p * work_loads.count(k) for k, p in points.items())

    if not count and not legacy:
        return 'These guys are already DevOps and in the Cloud and the business is happy!'
    return 'Burn baby burn disco inferno {} points earned in this roasting and {} complaints resolved!'.format(legacy, count)
