def cannons_ready(gunners):
    if 'nay' in gunners.values():
        return 'Shiver me timbers!'
    else:
        return 'Fire!'


cannons_ready({'m': 'a'})
