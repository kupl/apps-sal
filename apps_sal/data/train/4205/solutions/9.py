def cannons_ready(gunners):
    return 'Shiver me timbers!' if any((x == 'nay' for x in gunners.values())) else 'Fire!'
