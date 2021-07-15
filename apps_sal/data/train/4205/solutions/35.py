def cannons_ready(gunners):
    return 'Fire!' if list(gunners.values()).count('aye') == len(list(gunners.values())) else 'Shiver me timbers!'
