def cannons_ready(gunners):
    return "Fire!" if sum(1 if gunners[i] == 'aye' else 0 for i in gunners) == len(gunners) else 'Shiver me timbers!'
