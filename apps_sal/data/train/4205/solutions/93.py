def cannons_ready(gunners):
    gunners = list(gunners.values())
    if gunners.count("aye") == len(gunners):
        return("Fire!")
    if "nay" in gunners:
        return("Shiver me timbers!")
