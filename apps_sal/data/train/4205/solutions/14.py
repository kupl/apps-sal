def cannons_ready(gunners):
    values = list(gunners.values())
    count = 0
    for i in values:
        if i == 'nay':
            count += 1
        else:
            count += 0
    if count > 0:
        return 'Shiver me timbers!'
    return 'Fire!'
    

