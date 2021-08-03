def aa_percentage(*prot):
    if len(prot) > 1:
        sear = prot[1]
    else:
        sear = ["A", "I", "L", "M", "F", "W", "Y", "V"]
    times = 0
    for i in sear:
        times += prot[0].count(i)
    return round((times / len(prot[0])) * 100)
