def cannons_ready(gunners):
    return 'Fire!' if all((answer == 'aye' for answer in gunners.values())) else 'Shiver me timbers!'
