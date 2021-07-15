def cannons_ready(gunners):
    for answer in gunners:
        if gunners.get(answer) == 'nay':
            return 'Shiver me timbers!'
    return 'Fire!'

