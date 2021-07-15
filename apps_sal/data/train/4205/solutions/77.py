def cannons_ready(gunners: dict):
    return 'Fire!' if all([v.lower() == 'aye' for v in gunners.values()]) else 'Shiver me timbers!'
