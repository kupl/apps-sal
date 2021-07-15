def cannons_ready(gunners):
    return 'Fire!' if all(gun == 'aye' for gun in gunners.values()) else 'Shiver me timbers!'
