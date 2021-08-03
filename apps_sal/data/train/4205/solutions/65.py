def cannons_ready(gunners):
    temp = True
    for i in gunners:
        if gunners[i] == 'nay':
            temp = False
    return 'Fire!' if temp else 'Shiver me timbers!'
