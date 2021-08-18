def cannons_ready(gunners):
    if 'nay' not in list(gunners.values()):
        return 'Fire!'
    return 'Shiver me timbers!'
