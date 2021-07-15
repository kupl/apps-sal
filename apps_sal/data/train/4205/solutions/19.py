def cannons_ready(gunners):
    return 'Fire!' if all('aye' == el for el in gunners.values()) else 'Shiver me timbers!'
