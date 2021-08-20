def cannons_ready(gunners):
    flag = True
    for (key, value) in gunners.items():
        if value == 'nay':
            flag = False
            pass
    return 'Fire!' if flag else 'Shiver me timbers!'
