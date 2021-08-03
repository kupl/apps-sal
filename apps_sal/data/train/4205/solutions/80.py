def cannons_ready(gunners):
    return 'Fire!' if len(set(gunners.values())) <= 1 else 'Shiver me timbers!'
