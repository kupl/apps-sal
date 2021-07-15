def cannons_ready(gunners):
    if len(set(gunners.values())) == 1:
        return 'Fire!'
    return 'Shiver me timbers!'
