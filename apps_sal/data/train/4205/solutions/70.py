def cannons_ready(gunners):
    for name in gunners:
        if gunners.get(name) == 'nay':
            return 'Shiver me timbers!'
    return 'Fire!'
