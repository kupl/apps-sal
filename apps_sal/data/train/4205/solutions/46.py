def cannons_ready(gunners):
    flag = 0
    for value in list(gunners.values()):
        if value == 'aye':
            flag += 1
    return 'Fire!' if flag == len(gunners) else 'Shiver me timbers!'
