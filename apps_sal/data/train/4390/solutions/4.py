def fly_by(lamps, drone):
    ld = len(drone)
    ll = len(lamps)
    return 'o'*min(ld, ll) + 'x'*(ll - ld)
