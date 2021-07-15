def cannons_ready(gunners):
    if all(x == "aye" for x in gunners.values()):
        return "Fire!"
    if len(gunners) < 4:
        return "Shiver me timbers!"
    else:
        return "Fire!" if gunners["Mike"]== "aye" and gunners["Joe"] == "aye" and gunners["Johnson"] == "aye" and gunners["Peter"] == "aye" else "Shiver me timbers!"
