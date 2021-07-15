def cannons_ready(gunners):
    for gunner in list(gunners.values()):
        if gunner is not 'aye':
            return 'Shiver me timbers!'
    return 'Fire!'
