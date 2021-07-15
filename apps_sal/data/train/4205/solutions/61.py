def cannons_ready(gunners):
    fire = True
    for gunner in gunners:
        if gunners[gunner] == 'nay':
            fire = False
    return 'Fire!' if fire else 'Shiver me timbers!'
