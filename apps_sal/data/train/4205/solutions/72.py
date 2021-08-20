def cannons_ready(gunners):
    return 'Fire!' if all((i == 'aye' for i in gunners.values())) else 'Shiver me timbers!'
