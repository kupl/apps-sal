def cannons_ready(gunners):
    return 'Fire!' if all((v == 'aye' for v in gunners.values())) else 'Shiver me timbers!'
