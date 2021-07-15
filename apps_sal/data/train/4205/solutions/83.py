def cannons_ready(gunners):
    gunners = list(gunners.values())
    
    
    if gunners.count("nay") >= 1:
        return 'Shiver me timbers!'
    else:
        return "Fire!"
