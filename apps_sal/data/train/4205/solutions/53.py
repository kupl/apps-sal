def cannons_ready(gunners):
    if list(gunners.values()).count('nay') == 0:
        return 'Fire!'
    else:
        return 'Shiver me timbers!'
