def cannons_ready(gunners):
    b = list(gunners.values())
    if 'nay' not in b:
        return 'Fire!'
    else:
        return 'Shiver me timbers!'
