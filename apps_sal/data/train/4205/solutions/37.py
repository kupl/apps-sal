def cannons_ready(gunners):
    if any([x for x in list(gunners.values()) if x != 'aye']):
        return 'Shiver me timbers!'
    else:
        return 'Fire!'
