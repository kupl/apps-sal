def cannons_ready(gunners):
    print(gunners)
    if 'nay' in gunners.values():
        return 'Shiver me timbers!'
    else:
        return 'Fire!'
