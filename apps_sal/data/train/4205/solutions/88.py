def cannons_ready(gunners):
    return 'Fire!' if all((gunners[each] == 'aye' for each in gunners)) else 'Shiver me timbers!'
