def cannons_ready(gunners):
    for k, v in gunners.items():
        if all(v == 'aye' for v in gunners.values()):
            return 'Fire!'
        elif v == 'nay':
            return 'Shiver me timbers!'
