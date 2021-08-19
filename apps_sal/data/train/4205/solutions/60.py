def cannons_ready(gunners):
    nay_count = 0
    msg = 'Fire!'
    for (k, v) in gunners.items():
        if v == 'nay':
            nay_count += 1
    if nay_count:
        msg = 'Shiver me timbers!'
    return msg
