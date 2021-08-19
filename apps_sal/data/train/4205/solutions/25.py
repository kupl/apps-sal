def cannons_ready(gunners):
    return 'Shiver me timbers!' if 'nay' in [v for (k, v) in list(gunners.items())] else 'Fire!'
