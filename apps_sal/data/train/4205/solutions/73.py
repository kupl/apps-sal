def cannons_ready(gunners):
    for item in gunners:
        if gunners.get(item) == 'nay':
            return 'Shiver me timbers!'
    return 'Fire!'
