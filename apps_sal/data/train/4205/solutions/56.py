def cannons_ready(gunners):
    yes_or_no = list()
    for v in gunners.values():
        yes_or_no.append(v)
    if 'nay' in yes_or_no:
        return 'Shiver me timbers!'
    else:
        return 'Fire!'
