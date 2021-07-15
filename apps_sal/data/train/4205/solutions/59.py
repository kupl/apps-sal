def cannons_ready(gunners):
    msg = 'Fire!'
    if 'nay' in gunners.values():
        msg = 'Shiver me timbers!'
    return msg
