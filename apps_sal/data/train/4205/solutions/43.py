def cannons_ready(gunners):
    fire = {v: k for (k, v) in gunners.items()}
    z = fire.get('nay')
    return 'Fire!' if not z else 'Shiver me timbers!'
