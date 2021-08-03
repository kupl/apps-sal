def cannons_ready(gunners):
    result = 0
    for i in gunners:
        if gunners[i] == 'nay':
            result += 1
    return 'Fire!' if result == 0 else 'Shiver me timbers!'
