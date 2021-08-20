def cannons_ready(gunners):
    for ready in gunners.values():
        if ready == 'nay':
            return 'Shiver me timbers!'
    return 'Fire!'
