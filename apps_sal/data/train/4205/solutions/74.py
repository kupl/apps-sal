def cannons_ready(gunners):
    result = 'Fire!'
    for gun in gunners:
        if gunners[gun] == 'nay':
            result = 'Shiver me timbers!'
            break
    return result
