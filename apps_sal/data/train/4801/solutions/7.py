def roast_legacy(workloads):
    workloads = workloads.lower()
    complaints = sum( workloads.count(word) for word in ["slow!", "expensive!", "manual!", "down!", "hostage!", "security!"])
    legacy = sum( workloads.count(keyword)*points for (keyword,points) in [("cobol",1000), ("nonobject",500), ("monolithic",500), ("fax",100), ("modem",100), ("thickclient",50), ("tape",50), ("floppy",50), ("oldschoolit",50)])
    return 'These guys are already DevOps and in the Cloud and the business is happy!' if legacy+complaints==0 else 'Burn baby burn disco inferno %d points earned in this roasting and %d complaints resolved!' % (legacy,complaints)
