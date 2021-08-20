def cannons_ready(gunners):
    fire = True
    for (gunner, response) in gunners.items():
        if response == 'nay':
            fire = False
    return 'Fire!' if fire == True else 'Shiver me timbers!'
