def cannons_ready(gunners):
    if all([ready is 'aye' for (gunner, ready) in gunners.items()]):
        return 'Fire!'
    return 'Shiver me timbers!'
