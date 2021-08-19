def cannons_ready(gunners):
    return 'Fire!' if len(gunners) == list(gunners.values()).count('aye') else 'Shiver me timbers!'
