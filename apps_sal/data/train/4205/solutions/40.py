def cannons_ready(gunners):
    return 'Fire!' if all(['aye' == v for v in gunners.values()]) else 'Shiver me timbers!'
