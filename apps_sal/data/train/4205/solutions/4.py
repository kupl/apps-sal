def cannons_ready(gunners):
    return 'Fire!' if all((x == 'aye' for x in gunners.values())) else 'Shiver me timbers!'
