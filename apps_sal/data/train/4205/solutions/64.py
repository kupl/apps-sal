def cannons_ready(gunners):
    if all([True if i == 'aye' else False for i in gunners.values()]) == True:
        return 'Fire!'
    return 'Shiver me timbers!'
