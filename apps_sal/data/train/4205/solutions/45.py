def cannons_ready(gunners):
    if gunners and all((v == 'aye' for v in gunners.values())):
        return 'Fire!'
    else:
        return 'Shiver me timbers!'
