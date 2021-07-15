def cannons_ready(gunners):
    if all(a == 'aye' for a in gunners.values()):
        return 'Fire!'
    else:
        return 'Shiver me timbers!'
