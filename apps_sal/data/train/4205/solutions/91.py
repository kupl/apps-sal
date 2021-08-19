def cannons_ready(gunners):
    if len(set(gunners.values())) >= 2:
        return 'Shiver me timbers!'
    return 'Fire!'
