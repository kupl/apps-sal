def cannons_ready(gunners):
    l = gunners.values()
    m = [i for i in l]
    x = m.count('aye')
    y = m.count('nay')
    return 'Fire!' if x == len(m) else 'Shiver me timbers!'
