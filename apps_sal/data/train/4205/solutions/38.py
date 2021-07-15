def cannons_ready(gunners):
    
    g = gunners
    
    aye = [g[i] for i in g if g[i] == 'aye']
    nay = [g[i] for i in g if g[i] == 'nay']
    
    if len(nay) >= 1:
        return 'Shiver me timbers!'
    else:
        return 'Fire!'
