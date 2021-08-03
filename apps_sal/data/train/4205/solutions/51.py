def cannons_ready(gunners):
    return 'Shiver me timbers!' if sum([1 for k, v in list(gunners.items()) if v == "nay"]) else 'Fire!'
