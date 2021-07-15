def cannons_ready(gunners):
    if len(list(gunners.values())) <= list(gunners.values()).count('aye'):
        return 'Fire!'
    else:
        return 'Shiver me timbers!'
