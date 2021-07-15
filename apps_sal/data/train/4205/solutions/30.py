def cannons_ready(gunners):
    return 'Fire!' if not 'nay' in [gunners[i] for i in gunners] else 'Shiver me timbers!'
