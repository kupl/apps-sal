def cannons_ready(gunners):
    for gunner in gunners:
        if gunners.get(gunner) == 'nay':
            return 'Shiver me timbers!'
    return 'Fire!'
