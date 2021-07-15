def cannons_ready(gunners):
    return 'Fire!' if all(s == 'aye' for s in gunners.values()) else 'Shiver me timbers!'
