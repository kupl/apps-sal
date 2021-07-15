def cannons_ready(gunners):
    for i in gunners:
        if gunners[i] == 'nay':
            return 'Shiver me timbers!'
    else: return 'Fire!'
