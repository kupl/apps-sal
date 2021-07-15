def cannons_ready(gunners):
    for person, say in gunners.items():
        if say == 'nay':
            return 'Shiver me timbers!'
    return 'Fire!'
