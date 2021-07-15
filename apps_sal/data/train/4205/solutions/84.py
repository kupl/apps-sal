def cannons_ready(gunners):
    if list(set(gunners.values())) == ['aye']:
        return 'Fire!'
    else:
        return 'Shiver me timbers!'
